import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PresentationModesVariantes
        
class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(50, 50, 600, 600)
        self.setWindowTitle('2048')
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
        #57 caracteres
        self.label.setText("Le jeux consiste à faire apparaître la tuile « 2048 » en \ncombinant des nombres pairs sur une grille de 4 par 4 \ncases. Les seuls déplacements autorisés sont sur les \naxes verticaux et horizontaux. Chaque mouvement fait \napparaître une nouvelle tuile de chiffre 2. \n\n\nPour notre projet, nous avons decidé de faire \nune premiere page de présentation avec un bouton \ncredits, présentation et un bouton jouer qui \nredirige vers une page de différents choix \nde jeu. Ces jeux sont le 2048 en version originale, \n2 variantes d'interface et une variante de gameplay.")        
        self.label.resize(600,600)
        self.setDefaultButton = QPushButton("Présentation des modes", self)
        self.setDefaultButton.resize(350,50)
        self.setDefaultButton.move(self.width()/2 - 175,500)
        font=QFont('./Consolas',10,QFont.Bold)
        self.setDefaultButton.setFont(font)
        self.setDefaultButton.clicked.connect(self.clickMethodePresentation)

        self.setMenuBar()
        self.setCenter()
        self.show()
    def clickMethodePresentation(self):
        self.win2 = PresentationModesVariantes.Window2()

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


