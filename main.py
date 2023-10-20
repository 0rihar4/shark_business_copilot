import os
import sys
import time
from collections import defaultdict
from datetime import datetime

import joblib
from dotenv import load_dotenv
from PySide6 import QtCore
# from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QDialog, QDialogButtonBox,
                               QMainWindow, QMessageBox, QTableWidgetItem)

from conexao import GetInfosDB
from ui_functions import AuthUser
from ui_main import Ui_MainWindow
from ui_modal import Ui_Dialog
from ui_threads import DisparoThread, LoginThread, UpdateListThread

load_dotenv()


class DialogModal(QDialog, Ui_Dialog):
    def __init__(self, msg, parent=None) -> None:
        super().__init__()
        self.message = msg
        self.setupUi(self)
        self.setWindowTitle('Shark Copilot Avisa:')
        self.msg_modal.setText(str(msg))
        QBtn = QDialogButtonBox.Ok  # type:ignore
        self.buttonBox = QDialogButtonBox(QBtn)
        self.btn_confirm.accepted.connect(self.accept)

    def errorModal(self, title):
        error = QMessageBox.warning(self, title, self.message)
        if error == QDialogButtonBox.Ok:  # type:ignore
            self.close()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,) -> None:
        super(MainWindow, self).__init__()
        self.grupo_id = None
        self._my_errors = defaultdict(list)  # type:ignore
        # if self.logado:
        #     self.lineUser.setText('Logado')
        #     self.linePassword.setText('Logado')
        self.setupUi(self)
        self.setWindowTitle("Shark Copilot - Sistema de Disparos")
        appIcon = QIcon(u"ico_black.ico")
        self.loginProgress.hide()
        self.update_list_clientes.hide()

        self.worker_thread = None
        self.setWindowIcon(appIcon)
        ###############################################################
        # Check if the user is logged in
        self.isLogged()
        ###############################################################
        # TOGGLE BUTTON
        self.btn_toggle.clicked.connect(self.LeftMenu)
        # PAGINATION #############################################
        # PAG Oportunidades
        self.btn_oportunidades.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_oportunidades))
        # PAG Ajuda
        self.btn_cobranca.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_cobrancas))
        # PAG Ajuda
        self.btn_login.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_login))
        # PAG Ajuda
        self.btn_ajuda.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_ajuda))

        self.btn_logar.clicked.connect(self.start_authentication)
        ###################

        # Start Disparo
        self.bt_disparo.clicked.connect(
            self.DialogConfirmDisparo
        )
        # Atualizar Tabela
        self.btn_atualizar_clientes.clicked.connect(
            self.start_update_list_client
        )

    def DialogConfirmDisparo(self):
        mensagem = "Atenção! Nossa função de disparo realiza uma automação do whatsapp. Essa função pode ocasionar o bloqueamento do seu número!  \
        Utilize um numero de whatsapp secundario."  # noqa E501
        dlg = DialogModal(msg=mensagem, parent=self)

        # dlg.msg_modal.setText('Testando')
        if dlg.exec_():
            dlg.btn_confirm.clicked.connect(
                self.start_disparo()
            )

    def getInfosTable(self):
        dados_tabela = []
        num_linhas = self.table_select_clientes.rowCount()
        num_colunas = self.table_select_clientes.columnCount()

        # Percorre a tabela e coleta os dados
        for row in range(num_linhas):
            linha = {}
            for col in range(num_colunas):
                header = self.table_select_clientes.horizontalHeaderItem(
                    col).text()
                cell_data = self.table_select_clientes.item(row, col).text()
                linha[header] = cell_data
            dados_tabela.append(linha)
        return dados_tabela

    def configTableListClientes(self):

        try:
            auth = AuthUser()
            file_cache = str(os.getenv('LOGIN_CACHE'))
            auth.check_time_file_cache(file_cache)
            infos_login = joblib.load(os.getenv('LOGIN_CACHE'))
            id_user = infos_login.get('id', None)
            get_infos = GetInfosDB()
            try:
                infos_query = get_infos.get_files_csv(id_user)
                get_date_files = infos_query[1]
                # grupo_id = infos_query[0]
                num_linhas = len(get_date_files)  # type: ignore
                num_colunas = 3

                self.table_select_clientes.setRowCount(num_linhas)
                self.table_select_clientes.setColumnCount(num_colunas)

                headers = ['Nome', 'WhatsApp', 'Texto']
                self.table_select_clientes.setHorizontalHeaderLabels(headers)

                for row, (nome, info) in enumerate(
                        get_date_files.items()):  # type:ignore
                    self.table_select_clientes.setItem(
                        row, 0, QTableWidgetItem(nome))
                    self.table_select_clientes.setItem(
                        row, 1, QTableWidgetItem(info['whatsapp']))
                    self.table_select_clientes.setItem(
                        row, 2, QTableWidgetItem(info['texto']))
            except ValueError:
                self.table_select_clientes.setItem(
                    1, 0, QTableWidgetItem('Não Gerou Arquivos!'))
                self.table_select_clientes.setItem(
                    1, 1, QTableWidgetItem('Não Gerou Arquivos!'))
                self.table_select_clientes.setItem(
                    1, 2, QTableWidgetItem('Não Gerou Arquivos!'))

        except FileNotFoundError:
            ...

    def isLogged(self):
        try:
            auth = AuthUser()
            file_cache = str(os.getenv('LOGIN_CACHE'))
            auth.check_time_file_cache(file_cache)
            infos_login = joblib.load(os.getenv('LOGIN_CACHE'))

            user = infos_login.get('user', None)
            self.txt_user_login.setText(str(user))
            self.txt_data_login.setText(
                str(datetime.now().strftime('%d/%m/%Y'))
            )
            self.loginConfirmOpen(username=user)
            self.configTableListClientes()
        except FileNotFoundError:
            return False

    def LeftMenu(self):
        width = self.left_container.width()

        if width == 0:
            newWidth = 200
        else:
            newWidth = 0

        self.animation = QtCore.QPropertyAnimation(
            self.left_container, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(
            QtCore.QEasingCurve.InOutQuart  # type:ignore
        )
        self.animation.start()

    def set_infos_login(self):
        auth = AuthUser()
        try:
            infos_user = auth.get_infos_user()
        except Exception:
            file_cache = os.getenv('FILE_CACHE')
            auths_tokens = joblib.load(file_cache)
            refresh = auths_tokens['refresh']
            refresh_token = auth.refresh_token_user(refresh)
            if refresh_token:
                infos_user = auth.get_infos_user()
            else:
                infos_user = None
        print(infos_user)

    def authenticate_user(self):

        user = self.lineUser.text()
        password = self.linePassword.text()

        if user == '':
            self._my_errors['login'].append('Digite seu login')
        if password == '':
            self._my_errors['password'].append('Digite sua Senha')
        auth = AuthUser()
        login = auth.CR_token_login(user, password)
        if self._my_errors:
            text_errors = ''
            for key, erro in self._my_errors.items():
                text_errors += f'{erro[0]}\n'

            self.msg_error_login.setText(text_errors)
        else:
            if login:
                id_user = auth.get_infos_user()
                print(id_user)
                id_user = id_user[0].get('id', None)  # type:ignore
                infos_login = {
                    'id': id_user,
                    'user': user,
                    'password': password,

                }
                joblib.dump(infos_login, os.getenv('LOGIN_CACHE'))
                self.logado = True
                self.animationCloseBoxLogin()
                self.loginConfirmOpen(username=user)
                self.txt_user_login.setText(user)
                self.txt_data_login.setText(
                    str(datetime.now().strftime('%d/%m/%Y'))
                )
                self.msg_error_login.setText('')
                self.configTableListClientes()
            else:
                self.msg_error_login.setText('Usúario/Senha Inválidos')

    # Animation box login
    def loginConfirmOpen(self, **kwargs):
        self.boxLogin.setMaximumHeight(0)
        box_confirm_login_height = self.box_login_confirm.height()
        # Show Login Confirm Box
        self.animation = QtCore.QPropertyAnimation(
            self.box_login_confirm, b"maximumHeight")
        self.animation.setDuration(500)
        self.animation.setStartValue(box_confirm_login_height)
        self.animation.setEndValue(450)
        self.animation.setEasingCurve(
            QtCore.QEasingCurve.InOutQuart  # type:ignore
        )
        self.animation.start()
        username = kwargs.get('username', None)
        self.text_user_name.setText(str(username))

    def animationCloseBoxLogin(self):
        box_login_height = self.boxLogin.height()
        if box_login_height == 385:
            newHeight = 0
        else:
            newHeight = 385
        # Ocultar box login
        self.animation = QtCore.QPropertyAnimation(
            self.boxLogin, b"maximumHeight")
        self.animation.setDuration(500)
        self.animation.setStartValue(box_login_height)
        self.animation.setEndValue(newHeight)
        self.animation.setEasingCurve(
            QtCore.QEasingCurve.InOutQuart  # type:ignore
        )
        self.animation.start()

    # THREADS
    def start_authentication(self):
        user = self.lineUser.text()
        password = self.linePassword.text()

        if user == '' or password == '':
            self.msg_error_login.setText('Digite o usuário e a senha.')
            return

        self.loginProgress.show()
        self.loginProgress.setValue(0)
        self.btn_logar.setEnabled(False)

        self.worker_thread = LoginThread(user, password)
        self.worker_thread.finished.connect(self.authentication_finished)
        self.worker_thread.start()
        cont = 0
        while self.worker_thread.isFinished() is not True:
            self.loginProgress.setValue(cont)
            if cont < 100:
                cont += 1
            else:
                cont = 0
            time.sleep(0.001)

    def authentication_finished(self, success):
        self.loginProgress.hide()
        self.btn_logar.setEnabled(True)
        if success:
            user = self.lineUser.text()
            self.msg_error_login.setText('Autenticação bem-sucedida.')
            self.animationCloseBoxLogin()
            self.loginConfirmOpen(username=user)
            self.txt_user_login.setText(user)
            self.txt_data_login.setText(
                str(datetime.now().strftime('%d/%m/%Y'))
            )
            self.msg_error_login.setText('')
            self.configTableListClientes()

        else:
            self.msg_error_login.setText('Usuário/Senha Inválidos.')

    def start_update_list_client(self):
        table = self.table_select_clientes
        self.update_list_clientes.show()
        self.update_list_clientes.setValue(0)
        self.btn_atualizar_clientes.setEnabled(False)

        self.worker_thread = UpdateListThread(table=table)
        self.worker_thread.finished.connect(self.updates_list_client_finished)
        self.worker_thread.start()
        cont = 0
        while self.worker_thread.isFinished() is not True:
            self.update_list_clientes.setValue(cont)
            if cont < 100:
                cont += 1
            else:
                cont = 0
            time.sleep(0.001)

    def updates_list_client_finished(self, success):
        if success:
            self.update_list_clientes.hide()
            self.btn_atualizar_clientes.setEnabled(True)
        else:
            mensagem = "Ocorreu um erro ao Atualizar a Lista."
            dlg = DialogModal(msg=mensagem, parent=self)
            dlg.errorModal(title='Ocorreu um erro!')

    def start_disparo(self):
        dados = self.getInfosTable()
        progressBar = self.disparo_progress
        self.disparo_progress.setValue(0)
        self.bt_disparo.setText('Iniciando Disparo!')
        self.bt_disparo.setEnabled(False)

        self.worker_thread = DisparoThread(
            lista_disparo=dados, progressBar=progressBar
        )
        self.worker_thread.finished.connect(self.disparo_finished)
        self.worker_thread.start()

    def disparo_finished(self, success):
        self.disparo_progress.hide()
        self.bt_disparo.setText('Realizar Disparo!')
        self.bt_disparo.setEnabled(True)
        if success != []:
            for row, info in enumerate(
                    success):  # type:ignore
                self.table_result_clientes.setItem(
                    row, 0, QTableWidgetItem(info['Nome Cliente']))
                self.table_result_clientes.setItem(
                    row, 1, QTableWidgetItem(info['Whatsapp']))
                self.table_result_clientes.setItem(
                    row, 2, QTableWidgetItem(info['Status']))
        else:
            print('erro')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
