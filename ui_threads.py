
import os
from typing import Optional

import joblib
from dotenv import load_dotenv
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QProgressBar, QTableWidget, QTableWidgetItem

from conexao import GetInfosDB
from ui_automatizador import Disparo
from ui_functions import AuthUser

load_dotenv()


class LoginThread(QThread):
    finished = Signal(bool)

    def __init__(self, user, password) -> None:
        super().__init__()
        self.user = user
        self.password = password

    def run(self):
        auth = AuthUser()
        login = auth.CR_token_login(self.user, self.password)

        if login:
            id_user = auth.get_infos_user()
            id_user = id_user[0].get('id', None)
            infos_login = {
                'id': id_user,
                'user': self.user,
                'password': self.password,
            }
            joblib.dump(infos_login, os.getenv('LOGIN_CACHE'))
            self.finished.emit(True)
        else:
            self.finished.emit(False)


class UpdateListThread(QThread):
    finished = Signal(bool)

    def __init__(self, table: QTableWidget) -> None:
        super().__init__()
        self.table_select_clientes = table

    def run(self):
        try:
            auth = AuthUser()
            file_cache = str(os.getenv('LOGIN_CACHE'))
            auth.check_time_file_cache(file_cache)
            infos_login = joblib.load(os.getenv('LOGIN_CACHE'))
            id_user = infos_login.get('id', None)
            get_infos = GetInfosDB()
            get_date_files = get_infos.get_files_csv(id_user)
            num_linhas = len(get_date_files[1])  # type: ignore
            num_colunas = 3

            self.table_select_clientes.setRowCount(num_linhas)
            self.table_select_clientes.setColumnCount(num_colunas)

            headers = ['Nome', 'WhatsApp', 'Texto']
            self.table_select_clientes.setHorizontalHeaderLabels(headers)

            for row, infos in enumerate(get_date_files[1].items()):

                self.table_select_clientes.setItem(
                    row, 0, QTableWidgetItem(infos[0]))
                self.table_select_clientes.setItem(
                    row, 1, QTableWidgetItem(infos[1]['whatsapp']))
                self.table_select_clientes.setItem(
                    row, 2, QTableWidgetItem(infos[1]['texto']))
            self.finished.emit(True)

        except FileNotFoundError:
            self.finished.emit(False)


class DisparoThread(QThread):
    finished = Signal(list)

    def __init__(self, lista_disparo: list, progressBar: QProgressBar) -> None:
        super().__init__()
        self.progresso = progressBar
        self.dados = lista_disparo

    def run(self):
        disaprador = Disparo()
        finalizado = disaprador.disparar(
            lista_disparo=self.dados,
            callbakc=self.sendEmitProgress)
        if finalizado['success']:
            self.finished.emit(finalizado['mensagens'])
        else:
            self.finished.emit([])

    def sendEmitProgress(self):
        total = len(self.dados)
        porcentagem = (1*100)/total
        valor_atual = self.progresso.value()
        novo_valor = valor_atual + porcentagem
        self.progresso.setValue(int(novo_valor))
