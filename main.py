import sys

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)
botao = QPushButton('Texto Botão')

botao.show()
app.exec()
