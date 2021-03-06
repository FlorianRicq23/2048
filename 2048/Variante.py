import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from random import *


taille=4


    
def tour(board):

    index = choice(tuple(all_indices(board, 0)))
    return tuple(board[:index]) + (2,) + tuple(board[index+1:])
   
def shake(board, direction, max=2048):

    tailles = [*board]
    direction = direction.lower()
    if direction not in 'wasd':
        raise ValueError("{} does nothing".format(direction))

    for i in range(taille):
        
        if direction == 'a':
            start = i * taille
            end = start + taille
            tailles[start:end] = shake_taille(board[start:end], max)

        elif direction == 'd':
            start = i * taille - 1
            end = start + taille
            # -1 is the last element and not the one before the first one.
            # None must be used instead.
            if start == -1:
                start = None
            tailles[end:start:-1] = shake_taille(board[end:start:-1], max)

        elif direction in 'w':
            tailles[i::taille] = shake_taille(board[i::taille], max)

        elif direction in 's':
            start = (taille - 1) * taille + i
            tailles[start::-taille] = shake_taille(board[start::-taille], max)
    return tuple(tailles)


def shake_taille(taille, max=2048):
    l = len(taille)
    taille = [i for i in taille if i != 0]
    m = 1
    while m < max:
        indices = tuple(all_indices(taille, m))
        n = m*2
        for i in indices[:-1]:
            liste =[4,8,16,32,64,128,256,512,1024,2048]
            alea = choice(liste)
            if taille[i] == taille[i+1] == m:
                taille[i] = n
                taille[i+1] = None
            if taille[i] == alea:
                taille[i]=1
                
        taille = [i for i in taille if i is not None]
        m = n

    taille.extend([0] * (l - len(taille)))
    return tuple(taille)


def all_indices(haystack, needle):
    try:
        indice = -1
        while True:
            indice = haystack.index(needle, indice+1)
            yield indice
    except ValueError:
        pass



def setCenter(window):
    qr = window.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())

def main(window):
    app = QApplication(sys.argv)
    #window = QWidget()
    grille = QGridLayout()
    window.setGeometry(50, 50, 600, 600)
    window.setWindowTitle('2048')
    window.setFixedSize(600,600)
    setCenter(window)
    palette = QPalette()
    image=QImage("mario/background2.jpg")
    image=image.scaled(600,600)
    palette.setBrush(QPalette.Background,QBrush(image))
    window.setPalette(palette)

    labels = []
    for i in range(taille**2):
        label = QLabel("0")
        label.setAlignment(Qt.AlignCenter)
        labels.append(label)
        grille.addWidget(label, i // taille, i % taille)
    window.setLayout(grille)
    board = tuple([0] * taille**2)
    board = tour(tour(board))

    keys = {
        Qt.Key_Up: "w",
        Qt.Key_Left: "a",
        Qt.Key_Down: "s",
        Qt.Key_Right: "d",
    }

    def update():
        
        sizew=window.width()/4.4
        sizeh=window.height()/4.4      
        for i, v in enumerate(board): 
            labels[i].setText(str(v))
           
            if v==0:
                pixmap=QPixmap('mario/piece.png')
                small_pix=pixmap.scaled(sizew,sizeh)
                labels[i].setPixmap(small_pix)
            
            elif v==1:
                pixmap=QPixmap('mario/explosion.png')
                small_pix=pixmap.scaled(sizew,sizeh)
                labels[i].setPixmap(small_pix)
                
            elif v==2:
                pixmap=QPixmap('mario/perso2.png')
                small_pix=pixmap.scaled(sizew,sizeh)
                labels[i].setPixmap(small_pix)
   
            elif v==4:
                pixmap=QPixmap('mario/perso4.png')
                small_pix=pixmap.scaled(sizew,sizeh)
                labels[i].setPixmap(small_pix)
            elif v==8:
                pixmap=QPixmap('mario/perso8.png')
                small_pix=pixmap.scaled(sizew,sizeh)
                labels[i].setPixmap(small_pix)
            elif v==16:
                pixmap=QPixmap('mario/perso16.png')
                small_pix=pixmap.scaled(sizew,sizeh)
                labels[i].setPixmap(small_pix)
            elif v==32:
                pixmap=QPixmap('mario/perso32.png')
                small_pix=pixmap.scaled(sizew,sizeh)
                labels[i].setPixmap(small_pix)
            elif v==64:
                pixmap=QPixmap('mario/perso64.png')
                small_pix=pixmap.scaled(sizew,sizeh)
                labels[i].setPixmap(small_pix)
            elif v==128:
                pixmap=QPixmap('mario/perso128.png')
                small_pix=pixmap.scaled(sizew,sizeh)
                labels[i].setPixmap(small_pix)
            elif v==256:
                pixmap=QPixmap('mario/perso256.png')
                small_pix=pixmap.scaled(sizew,sizeh)
                labels[i].setPixmap(small_pix)
            elif v==512:
                pixmap=QPixmap('mario/perso512.png')
                small_pix=pixmap.scaled(sizew,sizeh)
                labels[i].setPixmap(small_pix)
            elif v==1024:
                pixmap=QPixmap('mario/perso1024.png')
                small_pix=pixmap.scaled(sizew,sizeh)
                labels[i].setPixmap(small_pix)
            elif v==2048:
                pixmap=QPixmap('mario/perso2048.png')
                small_pix=pixmap.scaled(sizew,sizeh)
                labels[i].setPixmap(small_pix)
           
         
        window.update()
    
    def key_press(event):
        nonlocal board
        
        key = event.key()
        try:
            w = keys[key] if key in keys else chr(key).lower()
        except ValueError:
            print("Key unknown {}".format(key), file=sys.stderr)
            return

        try:
            m = 4
            while m < 2048:
                new_board = shake(board, w, m)
                if new_board != board:
                    board = new_board
                    update()
                    app.processEvents()
                else:
                    board = new_board
                m *= 2
            update()
            app.processEvents()
            try:
                board = tour(board)
            except IndexError:
                msg_box = QMessageBox()
                msg_box.setText("Vous avez perdu")
                msg_box.exec_()
                board = tuple([0] * taille**2)
                board = tour(tour(board))

            update()
            app.processEvents()
        except ValueError:
            pass

    update()

    window.keyPressEvent = key_press
    window.show()

def jeu(window):
    main(window)


