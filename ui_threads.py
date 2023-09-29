
import os

import joblib
from dotenv import load_dotenv
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

from conexao import GetInfosDB
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
            self.finished.emit(True)

        except FileNotFoundError:
            self.finished.emit(False)
