from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_game(object):
    def setupUi(self, game):
        game.setObjectName("game")
        game.resize(515, 568)
        self.centralwidget = QtWidgets.QWidget(game)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.systemout = QtWidgets.QLabel(self.centralwidget)
        self.systemout.setGeometry(QtCore.QRect(80, 110, 151, 171))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.systemout.setFont(font)
        self.systemout.setFrameShape(QtWidgets.QFrame.Box)
        self.systemout.setAlignment(QtCore.Qt.AlignCenter)
        self.systemout.setObjectName("systemout")
        self.userout = QtWidgets.QLabel(self.centralwidget)
        self.userout.setGeometry(QtCore.QRect(290, 110, 151, 171))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.userout.setFont(font)
        self.userout.setFrameShape(QtWidgets.QFrame.Box)
        self.userout.setAlignment(QtCore.Qt.AlignCenter)
        self.userout.setObjectName("userout")
        self.rockbutton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it('rock'))
        self.rockbutton.setGeometry(QtCore.QRect(50, 300, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.rockbutton.setFont(font)
        self.rockbutton.setObjectName("rockbutton")
        self.paperbutton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it('paper'))
        self.paperbutton.setGeometry(QtCore.QRect(210, 300, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.paperbutton.setFont(font)
        self.paperbutton.setObjectName("paperbutton")
        self.scissorbutton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it('scissor'))
        self.scissorbutton.setGeometry(QtCore.QRect(370, 300, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.scissorbutton.setFont(font)
        self.scissorbutton.setObjectName("scissorbutton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 400, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 400, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 490, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(210, 490, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(360, 490, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.wincount = QtWidgets.QLabel(self.centralwidget)
        self.wincount.setGeometry(QtCore.QRect(110, 490, 47, 31))
        self.wincount.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wincount.setAlignment(QtCore.Qt.AlignCenter)
        self.wincount.setObjectName("wincount")
        self.drawcount = QtWidgets.QLabel(self.centralwidget)
        self.drawcount.setGeometry(QtCore.QRect(270, 490, 47, 31))
        self.drawcount.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.drawcount.setAlignment(QtCore.Qt.AlignCenter)
        self.drawcount.setObjectName("drawcount")
        self.losecount = QtWidgets.QLabel(self.centralwidget)
        self.losecount.setGeometry(QtCore.QRect(410, 490, 47, 31))
        self.losecount.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.losecount.setAlignment(QtCore.Qt.AlignCenter)
        self.losecount.setObjectName("losscount")
        game.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(game)
        self.statusbar.setObjectName("statusbar")
        game.setStatusBar(self.statusbar)

        self.retranslateUi(game)
        QtCore.QMetaObject.connectSlotsByName(game)

    def computer(self):
        lis={'rock','paper','scissor','rock','paper','scissor'}
        temp=[]
        for i in lis:
            temp.append(i)
        num=random.randint(0,2)
        systm=temp[num]
        return systm
    win=0
    lose=0
    Draw=0

    def press_it(self,pressed):
        if (pressed == 'rock') or (pressed == 'paper') or (pressed=='scissor') :
            self.userout.setText(pressed)
            syst=self.computer()
            self.systemout.setText(syst)
            if pressed == 'rock':
                if ((syst=='rock')):
                    self.Draw+=1
                    self.drawcount.setText(str(self.Draw))
                    self.label_2.setText('  Game Draw !!')
                elif(syst=='paper'):
                    self.lose+=1
                    self.losecount.setText(str(self.lose))
                    self.label_2.setText('  Lose')
                else:
                    self.win+=1
                    self.wincount.setText(str(self.win))
                    self.label_2.setText('  Won')
            elif pressed == 'paper':
                if ((syst=='paper')):
                    self.Draw+=1
                    self.drawcount.setText(str(self.Draw))
                    self.label_2.setText('  Game Draw !!')
                elif(syst=='scissor'):
                    self.lose+=1
                    self.losecount.setText(str(self.lose))
                    self.label_2.setText('  Lose')
                else:
                    self.win+=1
                    self.wincount.setText(str(self.win))
                    self.label_2.setText('  Won')
            elif pressed == 'scissor':
                if ((syst=='scissor')):
                    self.Draw+=1
                    self.drawcount.setText(str(self.Draw))
                    self.label_2.setText('  Game Draw !!')
                elif(syst=='rock'):
                    self.lose+=1
                    self.losecount.setText(str(self.lose))
                    self.label_2.setText('  Lose')
                else:
                    self.win+=1
                    self.wincount.setText(str(self.win))
                    self.label_2.setText('  Won')


    def retranslateUi(self, game):
        _translate = QtCore.QCoreApplication.translate
        game.setWindowTitle(_translate("game", "Game"))
        self.label.setText(_translate("game", "SYSTEM"))
        self.label_3.setText(_translate("game", "YOU"))
        self.systemout.setText(_translate("game", "Loading..."))
        self.userout.setText(_translate("game", "Click Button"))
        self.rockbutton.setText(_translate("game", "rock"))
        self.paperbutton.setText(_translate("game", "paper"))
        self.scissorbutton.setText(_translate("game", "scissor"))
        self.label_2.setText(_translate("game", "     output is loading..."))
        self.label_4.setText(_translate("game", "    Result :"))
        self.label_5.setText(_translate("game", "Win :"))
        self.label_6.setText(_translate("game", "Draw :"))
        self.label_7.setText(_translate("game", "Loss :"))
        self.wincount.setText(_translate("game", "0"))
        self.drawcount.setText(_translate("game", "0"))
        self.losecount.setText(_translate("game", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    game = QtWidgets.QMainWindow()
    ui = Ui_game()
    ui.setupUi(game)
    game.show()
    sys.exit(app.exec_())
