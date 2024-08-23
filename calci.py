from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui  import *
from PyQt5.QtWidgets import *
result=0


class Ui_MainWindow(QMainWindow):
   
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('logo.png'))

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(333, 420)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OutputLabel = QtWidgets.QLabel(self.centralwidget)
        self.OutputLabel.setGeometry(QtCore.QRect(10, 10, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.OutputLabel.setFont(font)
        self.OutputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.OutputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OutputLabel.setLineWidth(1)
        self.OutputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.OutputLabel.setObjectName("OutputLabel")
        self.button_7 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_but('7'))
        self.button_7.setGeometry(QtCore.QRect(10, 90, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_7.setFont(font)
        self.button_7.setObjectName("button_7")
        self.button_8 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_but('8'))
        self.button_8.setGeometry(QtCore.QRect(90, 90, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_8.setFont(font)
        self.button_8.setObjectName("button_8")
        self.button_9 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_but('9'))
        self.button_9.setGeometry(QtCore.QRect(170, 90, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_9.setFont(font)
        self.button_9.setObjectName("button_9")
        self.button_mul = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_but('*'))
        self.button_mul.setGeometry(QtCore.QRect(250, 90, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_mul.setFont(font)
        self.button_mul.setObjectName("button_mul")
        self.button_clear = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_but('C'))
        self.button_clear.setGeometry(QtCore.QRect(250, 10, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_clear.setFont(font)
        self.button_clear.setObjectName("button_clear")
        self.button_4 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_but('4'))
        self.button_4.setGeometry(QtCore.QRect(10, 170, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_4.setFont(font)
        self.button_4.setObjectName("button_4")
        self.button_5 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_but('5'))
        self.button_5.setGeometry(QtCore.QRect(90, 170, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_5.setFont(font)
        self.button_5.setObjectName("button_5")
        self.button_6 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_but('6'))
        self.button_6.setGeometry(QtCore.QRect(170, 170, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_6.setFont(font)
        self.button_6.setObjectName("button_6")
        self.button_add = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_but('+'))
        self.button_add.setGeometry(QtCore.QRect(250, 170, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_add.setFont(font)
        self.button_add.setObjectName("button_add")
        self.button_1 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_but('1'))
        self.button_1.setGeometry(QtCore.QRect(10, 250, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_1.setFont(font)
        self.button_1.setObjectName("button_1")
        self.button_2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_but('2'))
        self.button_2.setGeometry(QtCore.QRect(90, 250, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_2.setFont(font)
        self.button_2.setObjectName("button_2")
        self.button_3 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_but('3'))
        self.button_3.setGeometry(QtCore.QRect(170, 250, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_3.setFont(font)
        self.button_3.setObjectName("button_3")
        self.button_sub = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_but('-'))
        self.button_sub.setGeometry(QtCore.QRect(250, 250, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.button_sub.setFont(font)
        self.button_sub.setObjectName("button_sub")
        self.button_dot = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_but('.'))
        self.button_dot.setGeometry(QtCore.QRect(10, 330, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_dot.setFont(font)
        self.button_dot.setObjectName("button_dot")
        self.button_0 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_but('0'))
        self.button_0.setGeometry(QtCore.QRect(90, 330, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_0.setFont(font)
        self.button_0.setObjectName("button_0")
        self.button_divide = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_but('/'))
        self.button_divide.setGeometry(QtCore.QRect(170, 330, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_divide.setFont(font)
        self.button_divide.setObjectName("button_divide")
        self.button_result = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_but('='))
        self.button_result.setGeometry(QtCore.QRect(250, 330, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_result.setFont(font)
        self.button_result.setObjectName("button_result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def press_but(self,pressed):

        textc=self.OutputLabel.text()[-1]

        if (pressed == 'C'):
            self.OutputLabel.setText(' 0')
        elif(pressed == '='):
           if self.OutputLabel.text()[0].isdigit() and self.OutputLabel.text()[-1].isdigit():
                if self.OutputLabel.text().startswith('0')==True:
                  self.OutputLabel.setText(self.OutputLabel.text()[1:])
                equaal=eval(self.OutputLabel.text())
                global result
                result=str(equaal)
                self.OutputLabel.setText(f'{result}')
                print(self.OutputLabel.text(),' ',type(self.OutputLabel.text()))
                print(result,' ',type(result))
           
           
           elif self.OutputLabel.text()[0].isdigit() and (self.OutputLabel.text()[-1].isdigit()==False):
              if self.OutputLabel.text().startswith('0')==True:
                  self.OutputLabel.setText(self.OutputLabel.text()[1:])
              equaal2= eval(self.OutputLabel.text()[:-1])
              result2=str(format(equaal2,'.2f'))
              self.OutputLabel.setText(f'{result2}')

           elif self.OutputLabel.text()[0].isdigit()==False and (self.OutputLabel.text()[-1].isdigit()):
              equaal2= eval(self.OutputLabel.text()[1:])
              result2=str(format(equaal2,'.2f'))
              self.OutputLabel.setText(f'{result2}')

           elif (self.OutputLabel.text()[0].isdigit()==False) and (self.OutputLabel.text()[-1].isdigit()==False):
              temp=self.OutputLabel.text()[1:]
              equaal3= eval(temp[:-1])
              result3=str(format(equaal3,'.2f'))
              self.OutputLabel.setText(result3)
        
        elif (self.OutputLabel.text()==result):
               if pressed=='1' or pressed=='2' or pressed=='3' or pressed=='4' or pressed=='5' or  pressed=='6' or pressed=='7' or pressed=='8' or pressed=='9' or pressed=='0' :
                 self.OutputLabel.setText('')
                 self.OutputLabel.setText(pressed)
               elif pressed=='*' or pressed=='-' or pressed=='+' or pressed=='/' or pressed=='.':
                 self.OutputLabel.setText(f'{result}{pressed}')
                 

        elif( ( pressed=='*') or ( pressed=='+') or (pressed=='/') or (pressed=='-')or (pressed=='.')) and (( textc=='*') or ( textc=='+') or ( textc=='/') or ( textc=='-') or (textc=='')or (textc=='.')):
              (self.OutputLabel.setText(f'{self.OutputLabel.text()[:-1]}{pressed}'))
        else:
            if (self.OutputLabel.text()==(' 0')): # or self.OutputLabel.text()==result 
                 self.OutputLabel.setText('')
            self.OutputLabel.setText(f'{self.OutputLabel.text()}{pressed}')


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "calculator"))
        self.OutputLabel.setText(_translate("MainWindow", " 0"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_mul.setText(_translate("MainWindow", "X"))
        self.button_clear.setText(_translate("MainWindow", "C"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_add.setText(_translate("MainWindow", "+"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_sub.setText(_translate("MainWindow", "-"))
        self.button_dot.setText(_translate("MainWindow", "."))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_divide.setText(_translate("MainWindow", "/"))
        self.button_result.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())