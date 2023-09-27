import os
import sys
from collections import defaultdict

import joblib
from dotenv import load_dotenv
from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_functions import AuthUser
from ui_main import Ui_MainWindow

load_dotenv()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,) -> None:
        super(MainWindow, self).__init__()
        self.errors = defaultdict(list)
        # if self.logado:
        #     self.lineUser.setText('Logado')
        #     self.linePassword.setText('Logado')
        self.setupUi(self)
        self.setWindowTitle("Shark Copilot - Sistema de Disparos")
        appIcon = QIcon(u"")
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

        self.btn_logar.clicked.connect(self.authenticate_user)
        ###################

    def isLogged(self):
        try:
            auth = AuthUser()
            file_cache = str(os.getenv('LOGIN_CACHE'))
            auth.check_time_file_cache(file_cache)
            infos_login = joblib.load(os.getenv('LOGIN_CACHE'))
            user = infos_login.get('user', None)

            self.loginConfirmOpen(username=user)
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
            self.errors['login'].append('Digite seu login')
        if password == '':
            self.errors['password'].append('Digite sua Senha')
        auth = AuthUser()
        login = auth.CR_token_login(user, password)
        if self.errors:
            text_errors = ''
            for key, erro in self.errors.items():
                text_errors += f'{erro[0]}\n'

            self.msg_error_login.setText(text_errors)
        else:
            if login:
                infos_login = {
                    'user': user,
                    'password': password
                }
                joblib.dump(infos_login, os.getenv('LOGIN_CACHE'))
                self.logado = True
                self.animationCloseBoxLogin()
                self.loginConfirmOpen(username=user)
                self.msg_error_login.setText('')
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
        self.text_user_name.setText(username)

    def animationCloseBoxLogin(self):
        box_login_height = self.boxLogin.height()
        if box_login_height == 350:
            newHeight = 0
        else:
            newHeight = 350
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
