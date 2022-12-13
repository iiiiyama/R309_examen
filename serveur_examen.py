import socket
import sys
import threading
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout


# https://github.com/iiiiyama/R309_examen.git


host = ''
port = 10000
msg_client = ""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        grid = QVBoxLayout()
        widget.setLayout(grid)
        self.__lab1 = QLabel("serveur")
        self.__lab2 = QLabel("port")
        self.__lab3 = QLabel("nb de clients max")

        self.__text1 = QLineEdit("0.0.0.0")
        self.__text2 = QLineEdit("10000")
        self.__text3 = QLineEdit("5")
        self.__rep = QLabel(f' {self.__recep}\n')
        ok = QPushButton("démarrage du serveur")
        quit = QPushButton("quitter")
        arret = QPushButton("arrêt du serveur")

        grid.addWidget(self.__lab1)
        grid.addWidget(self.__lab2)
        grid.addWidget(self.__lab3)

        grid.addWidget(self.__text1)
        grid.addWidget(self.__text2)
        grid.addWidget(self.__text3)

        grid.addWidget(ok)
        grid.addWidget(self.__rep)
        grid.addWidget(quit)

        if ok.clicked:
           ok = arret

        ok.clicked.connect(self.__accept)
        quit.clicked.connect(self.__actionQuitter)
        self.setWindowTitle("le serveur de tchat")

        accept = threading.Thread(target=self.__accept)
        accept.start()

    def __actionQuitter(self):
        QCoreApplication.exit(0)

    def __arretserv(self):
        self.server_socket.close()
        print('le serveur est déconnecter')

    def __demarrage(self):
        self.server_socket = socket.socket()
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)

    def __accept(self):
        self.__demarrage = self.server_socket.accept()
        self.conn_client, self.client_address = self.server_socket.accept()

    def __recep(self):
        self.msg_client = self.conn_client.recv(1024).decode()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
