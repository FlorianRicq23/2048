#! /usr/bin/python3
# -*- coding: utf-8 -*-
#probleme des images qui se definissent a la meme taille
#barre de menu revenir a la page d'accueil 
#voit methode setText
#quitter une page quand on lance une autre
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


import Modes2048
import Presentation2048


class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.initUI()

    def initUI(self):
        self.setStyle(QStyleFactory.create('fusion'))
        palette = QPalette()
        image=QImage("images/background.jpg")
        image=image.scaled(600,600)
        palette.setBrush(QPalette.Background,QBrush(image)) 
        self.setPalette(palette)
        self.setWindowIcon(QIcon('images/icone.jpg'))
        
        
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(50, 50, 600, 600)
        self.setWindowTitle('2048')
        self.setFixedSize(600,600)

        self.setAffichage()
        self.setMenuBar()
        self.setCenter()
        self.show()
    
    def clickMethodPlay(self):
        self.win2 = Modes2048.Window2()
    
    def clickMethodPresentation(self):
        self.win2 = Presentation2048.Window2()
        
    
    def clickMethodCredits(self):
        QMessageBox.about(self, "Credit","Application créée dans le but d'un projet de semestre 2. \nFait par Florian Ricq, Enzo Marasa, Lucas Cecchini et Kamel El mazroui")

    def setAffichage(self):
        manette=QPixmap('images/logomanette.png')
        manette=manette.scaled(300,200)
        self.label=QLabel(self)
        self.label.setPixmap(manette)
        self.label.move(150,50)
        self.label.resize(300,200)

        self.buttonPlay = QPushButton("JOUER", self)
        self.buttonPlay.resize(200,64)
        self.buttonPlay.move(200,268)
        font=QFont('./Consolas',28,QFont.Bold)
        self.buttonPlay.setFont(font)
        self.buttonPlay.clicked.connect(self.clickMethodPlay)
        
        self.buttonModes = QPushButton("Présentation", self)
        self.buttonModes.resize(180,45)
        self.buttonModes.move(95,400)
        font=QFont('Consolas',15)
        self.buttonModes.setFont(font)
        self.buttonModes.clicked.connect(self.clickMethodPresentation)
        
        self.buttonCredits = QPushButton("Credits", self)
        self.buttonCredits.resize(140,45)
        self.buttonCredits.move(330,400)
        font=QFont('Consolas',15)
        self.buttonCredits.setFont(font)
        self.buttonCredits.clicked.connect(self.clickMethodCredits)

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
            

        


        

app = Application([])
win = Window()
app.exec_()


