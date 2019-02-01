import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

        
class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(50, 50, 600, 600)
        self.setWindowTitle('Présentation Modes et Variante')
        self.setFixedSize(600,600)
        p = self.palette();
        p.setColor(QPalette.Window, QColor(255,229,204))
        p.setColor(QPalette.WindowText, QColor(0,0,0))
    
        
        self.setPalette(p)
       
        
        self.label=QLabel(self)
        self.label.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.label.setAlignment(Qt.AlignCenter)
        font=QFont("Arial",14,QFont.Bold)
        self.label.setFont(font)

        self.label.setText("Variante : \n2048 modifié sous le theme de mario. \nUn nombre est généré aléatoirement parmis les \nnombres du 2048, si parmis les nombres additionnés \nil y a le nombre généré, alors cette case devient \nune bombe. Pour retransformer cette bombe il faut \nl'aditionner a une autre bombe et celles ci redeviennent \nune case de valeur 2. \n\nMode 1 : \n2048 avec les tuiles remplacées par des ordinateurs\n Apple du plus vieux au plus récent. \n\nMode 2 : \n2048 avec les tuiles remplacées par des consoles \nportable de la marque Nintendo de la plus vieille à la\nplus récente.")
        self.label.resize(600,600)

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

