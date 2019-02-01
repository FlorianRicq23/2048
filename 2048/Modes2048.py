from time import *
import sys
from random import choice
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Mode1
import Mode2
import Variante
import Jeu2048


class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(50, 50, 600, 600)
        self.setWindowTitle('2048')
        self.setFixedSize(600,600)
        
        hei=120
        widt=74
        pixmap2048=QPixmap('images/2048presentation.png')
        pixmap2048=pixmap2048.scaled(100,100)
        self.label=QLabel(self)
        self.label.setPixmap(pixmap2048)
        self.label.move(120,74)
        self.label.move(hei,widt)
        self.label.resize(102,102)        
        self.buttonModes = QPushButton("2048", self)
        self.buttonModes.resize(180,45)
        self.buttonModes.move(hei-40,widt + 110)
        font=QFont('Consolas',15)
        self.buttonModes.setFont(font)
        self.buttonModes.clicked.connect(self.clickMethod2048)
        
        hei=380
        widt=74
        pixmap2048=QPixmap('mario/logo.png')
        pixmap2048=pixmap2048.scaled(210,185)
        self.label=QLabel(self)
        self.label.setPixmap(pixmap2048)
        self.label.move(hei-50,widt-38)
        self.label.resize(210,185)        
        self.buttonModes = QPushButton("Variante", self)
        self.buttonModes.resize(180,45)
        self.buttonModes.move(hei-40,widt + 110)
        font=QFont('Consolas',15)
        self.buttonModes.setFont(font)
        self.buttonModes.clicked.connect(self.clickMethodVariante)

        
        hei=120
        widt=293
        pixmap2048=QPixmap('apple/apple.png')
        pixmap2048=pixmap2048.scaled(110,110)
        self.label=QLabel(self)
        self.label.setPixmap(pixmap2048)
        self.label.move(hei,widt-8)
        self.label.resize(110,110)        
        self.buttonModes = QPushButton("Mode 1", self)
        self.buttonModes.resize(180,45)
        self.buttonModes.move(hei-40,widt + 110)
        font=QFont('Consolas',15)
        self.buttonModes.setFont(font)
        self.buttonModes.clicked.connect(self.clickMethodMode1)
        
        hei=380
        widt=293
        pixmap2048=QPixmap('nintendo/nintendo2048.png')
        pixmap2048=pixmap2048.scaled(180,120)
        self.label=QLabel(self)
        self.label.setPixmap(pixmap2048)
        self.label.move(hei-40,widt+15)
        self.label.resize(180,102)        
        self.buttonModes = QPushButton("Mode 2", self)
        self.buttonModes.resize(180,45)
        self.buttonModes.move(hei-40,widt + 110)
        font=QFont('Consolas',15)
        self.buttonModes.setFont(font)
        self.buttonModes.clicked.connect(self.clickMethodMode2)
        
        self.label=QLabel(self)
        self.label.setPixmap(QPixmap('images/enjoy.png').scaled(200,100))
        self.label.move(200,470)
        self.label.resize(200,100)
        
        self.setMenuBar()
        self.setCenter()
        self.show()

    def setMenuBar(self):
        mainMenu = self.menuBar()
        self.exitAction=QAction("&Quitter", self, triggered=self.quitter)
        fileMenu=mainMenu.addMenu("Fichier")
        fileMenu.addAction(self.exitAction)


    def setCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def quitter(self):
        dialog=QMessageBox(self)
        
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(220,220,220))
        dialog.setPalette(palette)
        
        dialog.setText("Voulez-vous vraiment quitter ?")
        dialog.setWindowTitle("2048")

        dialog.setIcon(QMessageBox.Question)
        dialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        dialog.setDefaultButton(QMessageBox.Ok)
        if dialog.exec_()==QMessageBox.Ok:
            QApplication.instance().quit()

        
    def clickMethodMode1(self):
        Mode1.jeu(QWidget())
    def clickMethodMode2(self):
        Mode2.jeu(QWidget())
    def clickMethod2048(self):
        Jeu2048.jeu(QWidget())
    def clickMethodVariante(self):
        Variante.jeu(QWidget())
        




