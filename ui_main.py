# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'shark_copilot.ui'
##
# Created by: Qt User Interface Compiler version 6.5.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame,
                               QHBoxLayout, QHeaderView, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QSizePolicy,
                               QSpacerItem, QStackedWidget, QTableWidget,
                               QTableWidgetItem, QTextEdit, QToolBox,
                               QVBoxLayout, QWidget)

import icons_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1079, 785)
        MainWindow.setStyleSheet(u"background-color: rgb(25, 30, 46);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
                                         "	border:none;\n"
                                         "}\n"
                                         "QLabel{\n"
                                         "	color:white;\n"
                                         "}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMaximumSize(QSize(200, 16777215))
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_container)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, 9)
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame>QLabel{\n"
                                 "	width:30px;\n"
                                 "	border-bottom: 1px solid white;\n"
                                 "\n"
                                 "}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, 0, 0, 0)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(220, 220))
        self.label_2.setFrameShape(QFrame.VLine)
        self.label_2.setLineWidth(4)
        self.label_2.setMidLineWidth(6)
        self.label_2.setOpenExternalLinks(False)

        self.verticalLayout_4.addWidget(self.label_2)

        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_2.setStyleSheet(u"QToolBox{\n"
                                   "	font-size:17px;\n"
                                   "\n"
                                   "}\n"
                                   "QWidget{\n"
                                   "	color:white;\n"
                                   "}\n"
                                   "QWidget>QPushButton{\n"
                                   "	height:40px;\n"
                                   "	color:white;\n"
                                   "	font-size:15px;\n"
                                   "	border-bottom: 1px solid white;\n"
                                   "}\n"
                                   "QWidget>QPushButton:hover{\n"
                                   "	border-radius:5px;\n"
                                   "	background-color:white;\n"
                                   "	color:#313546;\n"
                                   "	border-bottom: none;\n"
                                   "}\n"
                                   "QWidget>QTextEdit{\n"
                                   "	text-aling:left;\n"
                                   "}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu = QWidget()
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(0, 0, 182, 519))
        self.menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayout_6 = QVBoxLayout(self.menu)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_login = QPushButton(self.menu)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMaximumSize(QSize(16777215, 40))
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.btn_login)

        self.btn_oportunidades = QPushButton(self.menu)
        self.btn_oportunidades.setObjectName(u"btn_oportunidades")
        self.btn_oportunidades.setMaximumSize(QSize(16777215, 40))
        self.btn_oportunidades.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.btn_oportunidades)

        self.btn_cobranca = QPushButton(self.menu)
        self.btn_cobranca.setObjectName(u"btn_cobranca")
        self.btn_cobranca.setMaximumSize(QSize(16777215, 40))
        self.btn_cobranca.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.btn_cobranca)

        self.btn_ajuda = QPushButton(self.menu)
        self.btn_ajuda.setObjectName(u"btn_ajuda")
        self.btn_ajuda.setMaximumSize(QSize(16777215, 40))
        self.btn_ajuda.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.btn_ajuda)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.menu, u"Menu")
        self.Inform = QWidget()
        self.Inform.setObjectName(u"Inform")
        self.Inform.setGeometry(QRect(0, 0, 182, 519))
        self.verticalLayout_7 = QVBoxLayout(self.Inform)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.textEdit = QTextEdit(self.Inform)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_7.addWidget(self.textEdit)

        self.toolBox.addItem(self.Inform, u"Informa\u00e7\u00f5es")

        self.verticalLayout_5.addWidget(self.toolBox)

        self.verticalLayout_3.addWidget(self.frame_2)

        self.horizontalLayout.addWidget(self.left_container)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setStyleSheet(
            u"background-color: rgb(49, 53, 70);")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(2, 0))
        self.top_frame.setStyleSheet(u"QFrame{\n"
                                     "	height:45px;\n"
                                     "	padding:5px;\n"
                                     "}\n"
                                     "QFrame>QLabel{\n"
                                     "	\n"
                                     "}")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setMinimumSize(QSize(100, 45))
        self.btn_toggle.setMaximumSize(QSize(150, 16777215))
        self.btn_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"D:/Space Marketing/Shark Business/1x/free-bars-1440391-1216351.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)

        self.title = QLabel(self.top_frame)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(16777215, 16777215))
        self.title.setStyleSheet(u"font-size:25px;")

        self.horizontalLayout_2.addWidget(self.title)

        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setStyleSheet(u"")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.main_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setCursor(QCursor(Qt.PointingHandCursor))
        self.Pages.setAutoFillBackground(False)
        self.Pages.setStyleSheet(u"background-color: rgb(49, 53, 70);\n"
                                 "")
        self.pg_oportunidades = QWidget()
        self.pg_oportunidades.setObjectName(u"pg_oportunidades")
        self.pg_oportunidades.setStyleSheet(
            u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout_3 = QHBoxLayout(self.pg_oportunidades)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_lista_disparo = QFrame(self.pg_oportunidades)
        self.frame_lista_disparo.setObjectName(u"frame_lista_disparo")
        self.frame_lista_disparo.setMaximumSize(QSize(16777215, 16777215))
        self.frame_lista_disparo.setFrameShape(QFrame.StyledPanel)
        self.frame_lista_disparo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_lista_disparo)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.btn_atualizar = QPushButton(self.frame_lista_disparo)
        self.btn_atualizar.setObjectName(u"btn_atualizar")
        self.btn_atualizar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_atualizar.setMouseTracking(False)
        self.btn_atualizar.setStyleSheet(u"color:#0B0F1B;\n"
                                         "font-weight: 600;\n"
                                         "background-color: #EEEEEE;\n"
                                         "padding:5px;\n"
                                         "border-radius:3px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/D:/Space Marketing/Shark Business/1x/refresh.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.btn_atualizar.setIcon(icon1)

        self.verticalLayout_10.addWidget(self.btn_atualizar, 0, Qt.AlignLeft)

        self.label_4 = QLabel(self.frame_lista_disparo)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 35))
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_4.setStyleSheet(u"color:rgb(25, 30, 46)")

        self.verticalLayout_10.addWidget(self.label_4)

        self.table_select_clientes = QTableWidget(self.frame_lista_disparo)
        if (self.table_select_clientes.columnCount() < 3):
            self.table_select_clientes.setColumnCount(3)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font)
        self.table_select_clientes.setHorizontalHeaderItem(
            0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font)
        self.table_select_clientes.setHorizontalHeaderItem(
            1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font)
        self.table_select_clientes.setHorizontalHeaderItem(
            2, __qtablewidgetitem2)
        if (self.table_select_clientes.rowCount() < 30):
            self.table_select_clientes.setRowCount(30)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_select_clientes.setVerticalHeaderItem(
            0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_select_clientes.setVerticalHeaderItem(
            1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_select_clientes.setVerticalHeaderItem(
            2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_select_clientes.setVerticalHeaderItem(
            3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_select_clientes.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_select_clientes.setItem(0, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_select_clientes.setItem(0, 2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_select_clientes.setItem(1, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_select_clientes.setItem(1, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_select_clientes.setItem(1, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_select_clientes.setItem(2, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_select_clientes.setItem(2, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_select_clientes.setItem(2, 2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_select_clientes.setItem(3, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_select_clientes.setItem(3, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_select_clientes.setItem(3, 2, __qtablewidgetitem18)
        self.table_select_clientes.setObjectName(u"table_select_clientes")
        self.table_select_clientes.setStyleSheet(u"QTableWidget{\n"
                                                 " border: 1px solid #ddd;\n"
                                                 "  padding: 8px;\n"
                                                 " border-radius:13px;\n"
                                                 " width: 100%;\n"
                                                 "alternate-background-color: #ededed;\n"
                                                 "selection-background-color: #282828;\n"
                                                 "\n"
                                                 "}\n"
                                                 "")
        self.table_select_clientes.setAlternatingRowColors(True)
        self.table_select_clientes.setSelectionMode(
            QAbstractItemView.SingleSelection)
        self.table_select_clientes.setSelectionBehavior(
            QAbstractItemView.SelectRows)
        self.table_select_clientes.setTextElideMode(Qt.ElideRight)
        self.table_select_clientes.setShowGrid(True)
        self.table_select_clientes.setGridStyle(Qt.SolidLine)
        self.table_select_clientes.setSortingEnabled(True)
        self.table_select_clientes.setRowCount(30)
        self.table_select_clientes.horizontalHeader().setVisible(False)
        self.table_select_clientes.horizontalHeader().setCascadingSectionResizes(False)
        self.table_select_clientes.horizontalHeader().setMinimumSectionSize(63)
        self.table_select_clientes.horizontalHeader().setDefaultSectionSize(150)
        self.table_select_clientes.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_10.addWidget(self.table_select_clientes)

        self.bt_disparo = QPushButton(self.frame_lista_disparo)
        self.bt_disparo.setObjectName(u"bt_disparo")
        self.bt_disparo.setMinimumSize(QSize(0, 40))
        self.bt_disparo.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_disparo.setStyleSheet(u"QPushButton{\n"
                                      "	background-color:#191E2E;\n"
                                      "	color:white;\n"
                                      "	border-radius:8px;\n"
                                      "	font-size:15px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "	background-color:#ccc;\n"
                                      "	color:#191E2E;\n"
                                      "	border:1px solid #191E2E;\n"
                                      "}\n"
                                      "")

        self.verticalLayout_10.addWidget(self.bt_disparo)

        self.horizontalLayout_3.addWidget(self.frame_lista_disparo)

        self.frame_msg_entregues = QFrame(self.pg_oportunidades)
        self.frame_msg_entregues.setObjectName(u"frame_msg_entregues")
        self.frame_msg_entregues.setFrameShape(QFrame.StyledPanel)
        self.frame_msg_entregues.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_msg_entregues)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.frame_msg_entregues)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setMaximumSize(QSize(16777215, 20))
        self.label_5.setStyleSheet(u"color:rgb(25, 30, 46)")

        self.verticalLayout_11.addWidget(self.label_5)

        self.table_result_clientes = QTableWidget(self.frame_msg_entregues)
        if (self.table_result_clientes.columnCount() < 3):
            self.table_result_clientes.setColumnCount(3)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_result_clientes.setHorizontalHeaderItem(
            0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_result_clientes.setHorizontalHeaderItem(
            1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_result_clientes.setHorizontalHeaderItem(
            2, __qtablewidgetitem21)
        if (self.table_result_clientes.rowCount() < 30):
            self.table_result_clientes.setRowCount(30)
        self.table_result_clientes.setObjectName(u"table_result_clientes")
        self.table_result_clientes.setStyleSheet(u"QTableWidget{\n"
                                                 " border: 1px solid #ddd;\n"
                                                 "  padding: 8px;\n"
                                                 " border-radius:13px;\n"
                                                 " width: 100%;\n"
                                                 "alternate-background-color: #ededed;\n"
                                                 "selection-background-color: #282828;\n"
                                                 "\n"
                                                 "}\n"
                                                 "")
        self.table_result_clientes.setAlternatingRowColors(True)
        self.table_result_clientes.setRowCount(30)
        self.table_result_clientes.horizontalHeader().setDefaultSectionSize(120)
        self.table_result_clientes.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_11.addWidget(self.table_result_clientes)

        self.horizontalLayout_3.addWidget(self.frame_msg_entregues)

        self.Pages.addWidget(self.pg_oportunidades)
        self.pg_cobrancas = QWidget()
        self.pg_cobrancas.setObjectName(u"pg_cobrancas")
        self.pg_cobrancas.setStyleSheet(
            u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout_4 = QHBoxLayout(self.pg_cobrancas)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_lista_disparo_2 = QFrame(self.pg_cobrancas)
        self.frame_lista_disparo_2.setObjectName(u"frame_lista_disparo_2")
        self.frame_lista_disparo_2.setMinimumSize(QSize(350, 568))
        self.frame_lista_disparo_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_lista_disparo_2.setFrameShape(QFrame.StyledPanel)
        self.frame_lista_disparo_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_lista_disparo_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.btn_atualizar_3 = QPushButton(self.frame_lista_disparo_2)
        self.btn_atualizar_3.setObjectName(u"btn_atualizar_3")
        self.btn_atualizar_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_atualizar_3.setStyleSheet(u"color:#0B0F1B;\n"
                                           "font-weight: 600;\n"
                                           "background-color: #EEEEEE;\n"
                                           "padding:5px;\n"
                                           "border-radius:3px;")
        self.btn_atualizar_3.setIcon(icon1)

        self.verticalLayout_15.addWidget(
            self.btn_atualizar_3, 0, Qt.AlignRight)

        self.label_9 = QLabel(self.frame_lista_disparo_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 20))
        self.label_9.setStyleSheet(u"color:rgb(25, 30, 46)")

        self.verticalLayout_15.addWidget(self.label_9)

        self.table_list_cobranca = QTableWidget(self.frame_lista_disparo_2)
        if (self.table_list_cobranca.columnCount() < 3):
            self.table_list_cobranca.setColumnCount(3)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_list_cobranca.setHorizontalHeaderItem(
            0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_list_cobranca.setHorizontalHeaderItem(
            1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_list_cobranca.setHorizontalHeaderItem(
            2, __qtablewidgetitem24)
        if (self.table_list_cobranca.rowCount() < 30):
            self.table_list_cobranca.setRowCount(30)
        self.table_list_cobranca.setObjectName(u"table_list_cobranca")
        self.table_list_cobranca.setStyleSheet(u"QTableWidget{\n"
                                               " border: 1px solid #ddd;\n"
                                               "  padding: 8px;\n"
                                               " border-radius:13px;\n"
                                               " width: 100%;\n"
                                               "alternate-background-color: #ededed;\n"
                                               "selection-background-color: #282828;\n"
                                               "\n"
                                               "}\n"
                                               "")
        self.table_list_cobranca.setAlternatingRowColors(True)
        self.table_list_cobranca.setSelectionMode(
            QAbstractItemView.SingleSelection)
        self.table_list_cobranca.setSelectionBehavior(
            QAbstractItemView.SelectRows)
        self.table_list_cobranca.setRowCount(30)
        self.table_list_cobranca.horizontalHeader().setDefaultSectionSize(150)
        self.table_list_cobranca.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_15.addWidget(self.table_list_cobranca)

        self.bt_disparo_3 = QPushButton(self.frame_lista_disparo_2)
        self.bt_disparo_3.setObjectName(u"bt_disparo_3")
        self.bt_disparo_3.setMinimumSize(QSize(100, 50))
        self.bt_disparo_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_disparo_3.setStyleSheet(u"QPushButton{\n"
                                        "	background-color:#191E2E;\n"
                                        "	color:white;\n"
                                        "	border-radius:8px;\n"
                                        "	font-size:15px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "	background-color:#ccc;\n"
                                        "	color:#191E2E;\n"
                                        "	border:1px solid #191E2E;\n"
                                        "}\n"
                                        "")

        self.verticalLayout_15.addWidget(self.bt_disparo_3)

        self.horizontalLayout_4.addWidget(self.frame_lista_disparo_2)

        self.frame_msg_entregues_2 = QFrame(self.pg_cobrancas)
        self.frame_msg_entregues_2.setObjectName(u"frame_msg_entregues_2")
        self.frame_msg_entregues_2.setFrameShape(QFrame.StyledPanel)
        self.frame_msg_entregues_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_msg_entregues_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_8 = QLabel(self.frame_msg_entregues_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 20))
        self.label_8.setStyleSheet(u"color:rgb(25, 30, 46)")

        self.verticalLayout_14.addWidget(self.label_8)

        self.table_result_cobranca = QTableWidget(self.frame_msg_entregues_2)
        if (self.table_result_cobranca.columnCount() < 3):
            self.table_result_cobranca.setColumnCount(3)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_result_cobranca.setHorizontalHeaderItem(
            0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_result_cobranca.setHorizontalHeaderItem(
            1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table_result_cobranca.setHorizontalHeaderItem(
            2, __qtablewidgetitem27)
        if (self.table_result_cobranca.rowCount() < 30):
            self.table_result_cobranca.setRowCount(30)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.table_result_cobranca.setVerticalHeaderItem(
            0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.table_result_cobranca.setVerticalHeaderItem(
            1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.table_result_cobranca.setVerticalHeaderItem(
            2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.table_result_cobranca.setVerticalHeaderItem(
            3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.table_result_cobranca.setVerticalHeaderItem(
            4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.table_result_cobranca.setVerticalHeaderItem(
            5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.table_result_cobranca.setItem(0, 0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.table_result_cobranca.setItem(0, 1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.table_result_cobranca.setItem(0, 2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.table_result_cobranca.setItem(1, 0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.table_result_cobranca.setItem(1, 1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.table_result_cobranca.setItem(1, 2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.table_result_cobranca.setItem(2, 0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.table_result_cobranca.setItem(2, 1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.table_result_cobranca.setItem(2, 2, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.table_result_cobranca.setItem(3, 0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.table_result_cobranca.setItem(3, 1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.table_result_cobranca.setItem(3, 2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.table_result_cobranca.setItem(4, 0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.table_result_cobranca.setItem(4, 1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.table_result_cobranca.setItem(4, 2, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.table_result_cobranca.setItem(5, 0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.table_result_cobranca.setItem(5, 1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.table_result_cobranca.setItem(5, 2, __qtablewidgetitem51)
        self.table_result_cobranca.setObjectName(u"table_result_cobranca")
        self.table_result_cobranca.setStyleSheet(u"QTableWidget{\n"
                                                 " border: 1px solid #ddd;\n"
                                                 "  padding: 8px;\n"
                                                 " border-radius:13px;\n"
                                                 " width: 100%;\n"
                                                 "alternate-background-color: #ededed;\n"
                                                 "selection-background-color: #282828;\n"
                                                 "\n"
                                                 "}\n"
                                                 "")
        self.table_result_cobranca.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        self.table_result_cobranca.setAlternatingRowColors(True)
        self.table_result_cobranca.setSelectionMode(
            QAbstractItemView.SingleSelection)
        self.table_result_cobranca.setSelectionBehavior(
            QAbstractItemView.SelectRows)
        self.table_result_cobranca.setRowCount(30)
        self.table_result_cobranca.horizontalHeader().setDefaultSectionSize(120)
        self.table_result_cobranca.horizontalHeader().setHighlightSections(True)
        self.table_result_cobranca.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_14.addWidget(self.table_result_cobranca)

        self.horizontalLayout_4.addWidget(self.frame_msg_entregues_2)

        self.Pages.addWidget(self.pg_cobrancas)
        self.pg_ajuda = QWidget()
        self.pg_ajuda.setObjectName(u"pg_ajuda")
        self.verticalLayout_9 = QVBoxLayout(self.pg_ajuda)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.Logo = QLabel(self.pg_ajuda)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setMaximumSize(QSize(16777215, 250))

        self.verticalLayout_9.addWidget(self.Logo)

        self.frame_4 = QFrame(self.pg_ajuda)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(1000, 16777215))
        self.label_6.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.label_6, 0, Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.frame_4, 0, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.pg_ajuda)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(250, 45))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
                                      "	background-color:#191E2E;\n"
                                      "	color:white;\n"
                                      "	border-radius:8px;\n"
                                      "	font-size:15px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "	background-color:#ccc;\n"
                                      "	color:#191E2E;\n"
                                      "	border:1px solid #191E2E;\n"
                                      "}\n"
                                      "")
        icon2 = QIcon()
        icon2.addFile(u":/icons/D:/Space Marketing/Shark Business/1x/whatsapp-icone-7.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)

        self.verticalLayout_9.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.Pages.addWidget(self.pg_ajuda)
        self.pg_login = QWidget()
        self.pg_login.setObjectName(u"pg_login")
        self.pg_login.setStyleSheet(u"QWidget>QPushButton{\n"
                                    "background-color:#191E2E;\n"
                                    "color:white;\n"
                                    "border-radius: 3px;\n"
                                    "font-size:17px;\n"
                                    "font-weight: 600;\n"
                                    "padding:8px;\n"
                                    "}\n"
                                    "QWidget>QPushButton:hover{\n"
                                    "background-color:white;\n"
                                    "color:#191E2E;\n"
                                    "}")
        self.verticalLayout_16 = QVBoxLayout(self.pg_login)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.container_logo = QFrame(self.pg_login)
        self.container_logo.setObjectName(u"container_logo")
        self.container_logo.setFrameShape(QFrame.StyledPanel)
        self.container_logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.container_logo)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_10 = QLabel(self.container_logo)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 100))
        self.label_10.setAlignment(Qt.AlignJustify | Qt.AlignTop)
        self.label_10.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_10)

        self.verticalLayout_16.addWidget(
            self.container_logo, 0, Qt.AlignVCenter)

        self.container_login = QFrame(self.pg_login)
        self.container_login.setObjectName(u"container_login")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(50)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.container_login.sizePolicy().hasHeightForWidth())
        self.container_login.setSizePolicy(sizePolicy1)
        self.container_login.setMinimumSize(QSize(0, 500))
        self.container_login.setFrameShape(QFrame.StyledPanel)
        self.container_login.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.container_login)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.boxLogin = QFrame(self.container_login)
        self.boxLogin.setObjectName(u"boxLogin")
        self.boxLogin.setMinimumSize(QSize(400, 0))
        self.boxLogin.setMaximumSize(QSize(16777215, 350))
        self.boxLogin.setStyleSheet(u"padding:5px;\n"
                                    "border:1px solid #121626;\n"
                                    "border-radius:13px")
        self.boxLogin.setFrameShape(QFrame.StyledPanel)
        self.boxLogin.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.boxLogin)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.msg_error_login = QLabel(self.boxLogin)
        self.msg_error_login.setObjectName(u"msg_error_login")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setBold(True)
        self.msg_error_login.setFont(font1)
        self.msg_error_login.setStyleSheet(u"border:none")

        self.verticalLayout_12.addWidget(
            self.msg_error_login, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.boxLogin)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"font-size:20px;\n"
                                   "margin-bottom:10px;\n"
                                   "border:none")

        self.verticalLayout_12.addWidget(self.label_3, 0, Qt.AlignBottom)

        self.lineUser = QLineEdit(self.boxLogin)
        self.lineUser.setObjectName(u"lineUser")
        self.lineUser.setMinimumSize(QSize(358, 0))
        self.lineUser.setMaximumSize(QSize(16777215, 80))
        self.lineUser.setStyleSheet(u"QLineEdit{\n"
                                    "background-color: rgb(49, 53, 70);\n"
                                    "border:1px solid white;\n"
                                    "color:white;\n"
                                    "border-radius: 8px;\n"
                                    "font-size:25px;\n"
                                    "padding:8px;\n"
                                    "margin-bottom:20px;\n"
                                    "}\n"
                                    "QLineEdit:focus{\n"
                                    "background:white;\n"
                                    "color: rgb(49, 53, 70);\n"
                                    "}")
        self.lineUser.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_12.addWidget(self.lineUser, 0, Qt.AlignVCenter)

        self.label_7 = QLabel(self.boxLogin)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 50))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"font-size:20px;\n"
                                   "border:none;\n"
                                   "margin-bottom:10px;")

        self.verticalLayout_12.addWidget(self.label_7)

        self.linePassword = QLineEdit(self.boxLogin)
        self.linePassword.setObjectName(u"linePassword")
        self.linePassword.setMinimumSize(QSize(358, 0))
        self.linePassword.setMaximumSize(QSize(16777215, 80))
        self.linePassword.setStyleSheet(u"QLineEdit{\n"
                                        "background-color: rgb(49, 53, 70);\n"
                                        "border:1px solid white;\n"
                                        "color:white;\n"
                                        "border-radius: 8px;\n"
                                        "font-size:25px;\n"
                                        "padding:8px;\n"
                                        "margin-bottom:20px;\n"
                                        "}\n"
                                        "QLineEdit:focus{\n"
                                        "background:white;\n"
                                        "color: rgb(49, 53, 70);\n"
                                        "}")
        self.linePassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_12.addWidget(self.linePassword)

        self.btn_logar = QPushButton(self.boxLogin)
        self.btn_logar.setObjectName(u"btn_logar")
        self.btn_logar.setMinimumSize(QSize(271, 0))
        self.btn_logar.setMaximumSize(QSize(16777215, 50))
        self.btn_logar.setStyleSheet(u"height:40px;")

        self.verticalLayout_12.addWidget(self.btn_logar)

        self.verticalLayout_19.addWidget(
            self.boxLogin, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.box_login_confirm = QFrame(self.container_login)
        self.box_login_confirm.setObjectName(u"box_login_confirm")
        self.box_login_confirm.setMinimumSize(QSize(450, 0))
        self.box_login_confirm.setMaximumSize(QSize(16777215, 0))
        self.box_login_confirm.setStyleSheet(u"padding:5px;\n"
                                             "border:1px solid #121626;\n"
                                             "border-radius:13px;\n"
                                             "margin-top:5px;")
        self.box_login_confirm.setFrameShape(QFrame.StyledPanel)
        self.box_login_confirm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.box_login_confirm)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.text_title_login = QLabel(self.box_login_confirm)
        self.text_title_login.setObjectName(u"text_title_login")
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.text_title_login.setFont(font3)
        self.text_title_login.setStyleSheet(u"border:none")
        self.text_title_login.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(
            self.text_title_login, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.text_user_name = QLabel(self.box_login_confirm)
        self.text_user_name.setObjectName(u"text_user_name")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(20)
        font4.setBold(False)
        self.text_user_name.setFont(font4)
        self.text_user_name.setStyleSheet(u"border:none")

        self.verticalLayout_17.addWidget(
            self.text_user_name, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.verticalLayout_19.addWidget(
            self.box_login_confirm, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.verticalLayout_16.addWidget(
            self.container_login, 0, Qt.AlignVCenter)

        self.Pages.addWidget(self.pg_login)

        self.verticalLayout_8.addWidget(self.Pages)

        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setMinimumSize(QSize(0, 50))
        self.footer_frame.setMaximumSize(QSize(16777215, 80))
        self.footer_frame.setStyleSheet(u"")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.footer_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.footer_frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        self.label.setStyleSheet(u"border-top: 1px solid #191E2E;")

        self.verticalLayout_2.addWidget(self.label)

        self.verticalLayout.addWidget(self.footer_frame)

        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(1)
        self.Pages.setCurrentIndex(3)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/D:/Space Marketing/Shark Business/1x/Icon - ,Shark Business - Automatic Copilot 2 c\u00f3pia.png\"/></p></body></html>", None))
# if QT_CONFIG(tooltip)
        self.toolBox.setToolTip(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Menu</p></body></html>", None))
# endif // QT_CONFIG(tooltip)
        self.btn_login.setText(QCoreApplication.translate(
            "MainWindow", u"Realizar Login", None))
        self.btn_oportunidades.setText(QCoreApplication.translate(
            "MainWindow", u"Oportunidades", None))
        self.btn_cobranca.setText(QCoreApplication.translate(
            "MainWindow", u"Cobran\u00e7as", None))
        self.btn_ajuda.setText(QCoreApplication.translate(
            "MainWindow", u"Ajuda", None))
        self.toolBox.setItemText(self.toolBox.indexOf(
            self.menu), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Usuario:</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Admin</span></p>\n"
                                                         "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; font-weight:600;\"><br /></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; ma"
                                                         "rgin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Sess\u00e3o:</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Ativa Chrome<br /></span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Vers\u00e3o Copilot:</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">1.0.0.0</span></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Inform), QCoreApplication.translate(
            "MainWindow", u"Informa\u00e7\u00f5es", None))
        self.btn_toggle.setText("")
        self.title.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Disparar Mensagens</span></p></body></html>", None))
        self.btn_atualizar.setText(QCoreApplication.translate(
            "MainWindow", u"Atualizar Lista", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Lista de Mensagens:</span></p></body></html>", None))
        ___qtablewidgetitem = self.table_select_clientes.horizontalHeaderItem(
            0)
        ___qtablewidgetitem.setText(QCoreApplication.translate(
            "MainWindow", u"Nome Cliente", None))
        ___qtablewidgetitem1 = self.table_select_clientes.horizontalHeaderItem(
            1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", u"Whatsapp", None))
        ___qtablewidgetitem2 = self.table_select_clientes.horizontalHeaderItem(
            2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", u"Mensagem", None))
        ___qtablewidgetitem3 = self.table_select_clientes.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("MainWindow", u"1", None))
        ___qtablewidgetitem4 = self.table_select_clientes.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("MainWindow", u"2", None))
        ___qtablewidgetitem5 = self.table_select_clientes.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate("MainWindow", u"3", None))
        ___qtablewidgetitem6 = self.table_select_clientes.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(
            QCoreApplication.translate("MainWindow", u"4", None))

        __sortingEnabled = self.table_select_clientes.isSortingEnabled()
        self.table_select_clientes.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.table_select_clientes.item(0, 0)
        ___qtablewidgetitem7.setText(
            QCoreApplication.translate("MainWindow", u"JO\u00e3o", None))
        ___qtablewidgetitem8 = self.table_select_clientes.item(0, 1)
        ___qtablewidgetitem8.setText(
            QCoreApplication.translate("MainWindow", u"1", None))
        ___qtablewidgetitem9 = self.table_select_clientes.item(0, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate(
            "MainWindow", u"LoremLoremLoremLoremLoremLoremLoremLoremLorem", None))
        ___qtablewidgetitem10 = self.table_select_clientes.item(1, 0)
        ___qtablewidgetitem10.setText(
            QCoreApplication.translate("MainWindow", u"Clara", None))
        ___qtablewidgetitem11 = self.table_select_clientes.item(1, 1)
        ___qtablewidgetitem11.setText(
            QCoreApplication.translate("MainWindow", u"2", None))
        ___qtablewidgetitem12 = self.table_select_clientes.item(1, 2)
        ___qtablewidgetitem12.setText(
            QCoreApplication.translate("MainWindow", u"2", None))
        ___qtablewidgetitem13 = self.table_select_clientes.item(2, 0)
        ___qtablewidgetitem13.setText(
            QCoreApplication.translate("MainWindow", u"Paulo", None))
        ___qtablewidgetitem14 = self.table_select_clientes.item(2, 1)
        ___qtablewidgetitem14.setText(
            QCoreApplication.translate("MainWindow", u"3", None))
        ___qtablewidgetitem15 = self.table_select_clientes.item(2, 2)
        ___qtablewidgetitem15.setText(
            QCoreApplication.translate("MainWindow", u"3", None))
        ___qtablewidgetitem16 = self.table_select_clientes.item(3, 0)
        ___qtablewidgetitem16.setText(
            QCoreApplication.translate("MainWindow", u"4", None))
        ___qtablewidgetitem17 = self.table_select_clientes.item(3, 1)
        ___qtablewidgetitem17.setText(
            QCoreApplication.translate("MainWindow", u"4", None))
        ___qtablewidgetitem18 = self.table_select_clientes.item(3, 2)
        ___qtablewidgetitem18.setText(
            QCoreApplication.translate("MainWindow", u"4", None))
        self.table_select_clientes.setSortingEnabled(__sortingEnabled)

        self.bt_disparo.setText(QCoreApplication.translate(
            "MainWindow", u"Realizar Disparo", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Mensagens Entregues:</span></p></body></html>", None))
        ___qtablewidgetitem19 = self.table_result_clientes.horizontalHeaderItem(
            0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate(
            "MainWindow", u"Nome Cliente", None))
        ___qtablewidgetitem20 = self.table_result_clientes.horizontalHeaderItem(
            1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate(
            "MainWindow", u"Oportunidade", None))
        ___qtablewidgetitem21 = self.table_result_clientes.horizontalHeaderItem(
            2)
        ___qtablewidgetitem21.setText(
            QCoreApplication.translate("MainWindow", u"Status", None))
        self.btn_atualizar_3.setText(QCoreApplication.translate(
            "MainWindow", u"Atualizar Lista", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Lista de Cobran\u00e7as:</span></p></body></html>", None))
        ___qtablewidgetitem22 = self.table_list_cobranca.horizontalHeaderItem(
            0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate(
            "MainWindow", u"Nome da Lista", None))
        ___qtablewidgetitem23 = self.table_list_cobranca.horizontalHeaderItem(
            1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate(
            "MainWindow", u"Data Cria\u00e7\u00e3o", None))
        ___qtablewidgetitem24 = self.table_list_cobranca.horizontalHeaderItem(
            2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate(
            "MainWindow", u"Selecionar Lista", None))
        self.bt_disparo_3.setText(QCoreApplication.translate(
            "MainWindow", u"Realizar Disparo", None))
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Cobran\u00e7as Entregues:</span></p></body></html>", None))
        ___qtablewidgetitem25 = self.table_result_cobranca.horizontalHeaderItem(
            0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate(
            "MainWindow", u"Nome Cliente", None))
        ___qtablewidgetitem26 = self.table_result_cobranca.horizontalHeaderItem(
            1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate(
            "MainWindow", u"Oportunidade", None))
        ___qtablewidgetitem27 = self.table_result_cobranca.horizontalHeaderItem(
            2)
        ___qtablewidgetitem27.setText(
            QCoreApplication.translate("MainWindow", u"Status", None))
        ___qtablewidgetitem28 = self.table_result_cobranca.verticalHeaderItem(
            0)
        ___qtablewidgetitem28.setText(
            QCoreApplication.translate("MainWindow", u"1", None))
        ___qtablewidgetitem29 = self.table_result_cobranca.verticalHeaderItem(
            1)
        ___qtablewidgetitem29.setText(
            QCoreApplication.translate("MainWindow", u"2", None))
        ___qtablewidgetitem30 = self.table_result_cobranca.verticalHeaderItem(
            2)
        ___qtablewidgetitem30.setText(
            QCoreApplication.translate("MainWindow", u"2", None))
        ___qtablewidgetitem31 = self.table_result_cobranca.verticalHeaderItem(
            3)
        ___qtablewidgetitem31.setText(
            QCoreApplication.translate("MainWindow", u"3", None))
        ___qtablewidgetitem32 = self.table_result_cobranca.verticalHeaderItem(
            4)
        ___qtablewidgetitem32.setText(
            QCoreApplication.translate("MainWindow", u"4", None))
        ___qtablewidgetitem33 = self.table_result_cobranca.verticalHeaderItem(
            5)
        ___qtablewidgetitem33.setText(
            QCoreApplication.translate("MainWindow", u"6", None))

        __sortingEnabled1 = self.table_result_cobranca.isSortingEnabled()
        self.table_result_cobranca.setSortingEnabled(False)
        ___qtablewidgetitem34 = self.table_result_cobranca.item(0, 0)
        ___qtablewidgetitem34.setText(
            QCoreApplication.translate("MainWindow", u"Lorem", None))
        ___qtablewidgetitem35 = self.table_result_cobranca.item(0, 1)
        ___qtablewidgetitem35.setText(
            QCoreApplication.translate("MainWindow", u"Lorem", None))
        ___qtablewidgetitem36 = self.table_result_cobranca.item(0, 2)
        ___qtablewidgetitem36.setText(
            QCoreApplication.translate("MainWindow", u"Lorem", None))
        ___qtablewidgetitem37 = self.table_result_cobranca.item(1, 0)
        ___qtablewidgetitem37.setText(
            QCoreApplication.translate("MainWindow", u"Lorem", None))
        ___qtablewidgetitem38 = self.table_result_cobranca.item(1, 1)
        ___qtablewidgetitem38.setText(
            QCoreApplication.translate("MainWindow", u"Lorem", None))
        ___qtablewidgetitem39 = self.table_result_cobranca.item(1, 2)
        ___qtablewidgetitem39.setText(
            QCoreApplication.translate("MainWindow", u"Lorem", None))
        ___qtablewidgetitem40 = self.table_result_cobranca.item(2, 0)
        ___qtablewidgetitem40.setText(
            QCoreApplication.translate("MainWindow", u"Lorem", None))
        ___qtablewidgetitem41 = self.table_result_cobranca.item(2, 1)
        ___qtablewidgetitem41.setText(
            QCoreApplication.translate("MainWindow", u"Lorem", None))
        ___qtablewidgetitem42 = self.table_result_cobranca.item(2, 2)
        ___qtablewidgetitem42.setText(
            QCoreApplication.translate("MainWindow", u"Lorem", None))
        ___qtablewidgetitem43 = self.table_result_cobranca.item(3, 0)
        ___qtablewidgetitem43.setText(
            QCoreApplication.translate("MainWindow", u"Lorem", None))
        ___qtablewidgetitem44 = self.table_result_cobranca.item(3, 1)
        ___qtablewidgetitem44.setText(
            QCoreApplication.translate("MainWindow", u"Lorem", None))
        ___qtablewidgetitem45 = self.table_result_cobranca.item(3, 2)
        ___qtablewidgetitem45.setText(
            QCoreApplication.translate("MainWindow", u"Lorem", None))
        ___qtablewidgetitem46 = self.table_result_cobranca.item(4, 0)
        ___qtablewidgetitem46.setText(
            QCoreApplication.translate("MainWindow", u"Lorem", None))
        ___qtablewidgetitem47 = self.table_result_cobranca.item(4, 1)
        ___qtablewidgetitem47.setText(
            QCoreApplication.translate("MainWindow", u"Lorem", None))
        ___qtablewidgetitem48 = self.table_result_cobranca.item(4, 2)
        ___qtablewidgetitem48.setText(
            QCoreApplication.translate("MainWindow", u"Lorem", None))
        ___qtablewidgetitem49 = self.table_result_cobranca.item(5, 0)
        ___qtablewidgetitem49.setText(
            QCoreApplication.translate("MainWindow", u"Lorem", None))
        ___qtablewidgetitem50 = self.table_result_cobranca.item(5, 1)
        ___qtablewidgetitem50.setText(
            QCoreApplication.translate("MainWindow", u"Lorem", None))
        ___qtablewidgetitem51 = self.table_result_cobranca.item(5, 2)
        ___qtablewidgetitem51.setText(
            QCoreApplication.translate("MainWindow", u"Lorem", None))
        self.table_result_cobranca.setSortingEnabled(__sortingEnabled1)

        self.Logo.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/D:/Space Marketing/Shark Business/1x/Shark Business - Automatic Copilot 3.png\" /></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Lorem Ipsum:</span></p><p><br/></p><p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p><p><br/></p><p><br/></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate(
            "MainWindow", u"Chamar Suporte", None))
        self.label_10.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/D:/Space Marketing/Shark Business/1x/Shark Business - Automatic Copilot 3.png\"/></p></body></html>", None))
        self.msg_error_login.setText("")
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"Digite o seu Login:", None))
        self.lineUser.setInputMask("")
        self.lineUser.setText("")
        self.lineUser.setPlaceholderText("")
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"Digite sua Senha:", None))
        self.btn_logar.setText(QCoreApplication.translate(
            "MainWindow", u"Realizar login com Shark Business\u00ae", None))
        self.text_title_login.setText(QCoreApplication.translate(
            "MainWindow", u"Voc\u00ea Est\u00e1 Logado com:", None))
        self.text_user_name.setText(QCoreApplication.translate(
            "MainWindow", u"@Nome_Usuario", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/D:/Space Marketing/Shark Business/1x/AQUIIII.png\"/></p></body></html>", None))
    # retranslateUi
