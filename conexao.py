import csv
import os

import paramiko
import psycopg2
from dotenv import load_dotenv
from sshtunnel import SSHTunnelForwarder

load_dotenv()
# Defining variables for access ssh on server and data base


# class ConnectionDB():
# Create ssh connection
class ConnectionDB():
    def __init__(self) -> None:
        self.db_host = "localhost"
        self.db_name = os.getenv("BD_NAME")
        self.db_user = os.getenv("BD_USER")
        self.db_password = os.getenv("BD_PASSWORD")
        self.db_port = int(os.getenv("BD_PORTA"))  # type:ignore

        self.ssh_host = os.getenv('SSH_HOST')
        self.ssh_port = int(os.getenv('SSH_PORT'))  # type:ignore
        self.ssh_user = os.getenv("SSH_USER")
        self.ssh_password = os.getenv("SSH_PASSWORD")

    def AccessDataBase(self, comando_sql):
        conn = None
        cursor = None
        with SSHTunnelForwarder(
            (self.ssh_host, self.ssh_port),
            ssh_username=self.ssh_user,
            ssh_password=self.ssh_password,
            remote_bind_address=(self.db_host, self.db_port),
        ) as tunnel:
            # Conectar ao banco de dados PostgreSQL através do túnel SSH
            try:
                conn = psycopg2.connect(
                    database=self.db_name,
                    user=self.db_user,
                    password=self.db_password,
                    host="127.0.0.1",
                    port=tunnel.local_bind_port,  # type:ignore
                )
                cursor = conn.cursor()
                cursor.execute("SELECT version();")
                version = cursor.fetchone()
                print("Versão do PostgreSQL:", version[0])
                cursor.execute(comando_sql)
                try:
                    conn.commit()
                    print('Requisição feita com sucesso!')
                except Exception as e:
                    print(e)
            except psycopg2.OperationalError as e:
                return str(e)
            finally:
                if cursor is not None:
                    cursor.close()
                if conn is not None:
                    conn.close()

    def ConsultDataBase(self, tabela, colunas, where=None):
        conn = None
        cursor = None
        with SSHTunnelForwarder(
            (self.ssh_host, self.ssh_port),
            ssh_username=self.ssh_user,
            ssh_password=self.ssh_password,
            remote_bind_address=(self.db_host, self.db_port),
        ) as tunnel:
            # Conectar ao banco de dados PostgreSQL através do túnel SSH
            try:
                conn = psycopg2.connect(
                    database=self.db_name,
                    user=self.db_user,
                    password=self.db_password,
                    host="127.0.0.1",
                    port=tunnel.local_bind_port,  # type:ignore
                )
                cursor = conn.cursor()
                # consulta_sql = f"SELECT {', '.join(colunas)} FROM {tabela}"
                if where is not None:
                    consulta_sql = f"SELECT {', '.join(colunas)} FROM {tabela} WHERE {where}"  # noqa E501
                else:
                    consulta_sql = f"SELECT {', '.join(colunas)} FROM {tabela}"

                print(consulta_sql)
                cursor.execute(consulta_sql)
                resultados = cursor.fetchall()
                print(resultados)
                return resultados
            except psycopg2.OperationalError as e:
                return str(e)
            finally:
                if cursor is not None:
                    cursor.close()
                if conn is not None:
                    conn.close()

    def GetCsvFile(self, remote_file_path, local_file_path):
        try:
            # Criar uma conexão SSH
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(self.ssh_host, self.ssh_port,
                               self.ssh_user, self.ssh_password)
            with ssh_client.open_sftp() as sftp:
                sftp.get(remote_file_path, local_file_path)
            with open(local_file_path, 'r', newline='', encoding='utf-8') as csv_file:  # noqa E501
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    print(row)
            os.remove(local_file_path)

            # Fechar a conexão SSH
            ssh_client.close()

        except Exception as e:
            print(e)
            return f"Erro ao ler o arquivo CSV: {str(e)}"


if __name__ == '__main__':
    conn = ConnectionDB()
    comando_sql = """
    SELECT `csv` FROM `disparo_disparfilescsv`
    """
    where = """ disparo_disparfilescsv.empresa_id = 2 """
    colunas = ['csv', 'disparo_disparfilescsv.grupo_arquivo_id']
    sql = conn.ConsultDataBase(
        tabela='disparo_disparfilescsv',
        colunas=colunas,
        where=where)
    if sql != []:
        for linha in sql:
            remote_file_path = f"sharkapp/media/{linha[0]}"
            file_name = linha[0].split('/')
            file_name = file_name[1]
            print(file_name)
            csv_file = conn.GetCsvFile(remote_file_path, file_name)
    else:
        print('Esse Cliente não gerou arquivos!')
