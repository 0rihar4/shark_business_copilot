# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modal_dialog_box.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(410, 169)
        Dialog.setStyleSheet(u"color:white;\n"
"background-color: rgb(38, 44, 67);\n"
"border:none;")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"color:white")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.msg_modal = QLabel(self.frame)
        self.msg_modal.setObjectName(u"msg_modal")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        self.msg_modal.setFont(font1)
        self.msg_modal.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.msg_modal)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"Line{\n"
"padding: 22px;\n"
"background:#101426;\n"
"}")
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(5)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout_2.addWidget(self.line)

        self.btn_confirm = QDialogButtonBox(self.frame)
        self.btn_confirm.setObjectName(u"btn_confirm")
        self.btn_confirm.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_confirm.setStyleSheet(u"\n"
"color:#566187;\n"
"border: 1px solid #566187;\n"
"width:350px;\n"
"height:30px;\n"
"border-radius: 6px;\n"
"\n"
"")
        self.btn_confirm.setStandardButtons(QDialogButtonBox.Ok)
        self.btn_confirm.setCenterButtons(True)

        self.verticalLayout_2.addWidget(self.btn_confirm, 0, Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.msg_modal.setText(QCoreApplication.translate("Dialog", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi at condimentum quam. ", None))
    # retranslateUi

