import sys
import mysql.connector
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, 
                             QListWidget, QLineEdit, QLabel, QMessageBox, QInputDialog)

# file run by database and pyqt5 ,mysql-connector-python

class Todo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.frontend()
        self.connectionDB()
        self.createTable()
        self.viewtodo()
  
    def frontend(self):

        self.setWindowTitle('To-Do Application')
        self.setGeometry(550, 170, 350, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        self.inputbox=QLineEdit()
        self.layout.addWidget(self.inputbox)

        self.add_button = QPushButton('INSERT')
        self.add_button.clicked.connect(self.addtodo)
        self.layout.addWidget(self.add_button)

        self.layout.addWidget(QLabel('TODO List'))
        self.viewtask = QListWidget()
        self.layout.addWidget(self.viewtask)

        self.update_task_button = QPushButton('update Task')
        self.update_task_button.clicked.connect(self.updatetask)
        self.layout.addWidget(self.update_task_button)

        self.delete_task_button = QPushButton('Delete Task')
        self.delete_task_button.clicked.connect(self.deletetask)
        self.layout.addWidget(self.delete_task_button)
        
        self.central_widget.setLayout(self.layout)

    def connectionDB(self):
       try: 
            self.mydb=mysql.connector.connect(host='127.0.0.1',user='root',password='root',port=3307,database='yamaha')
            if self.mydb.is_connected():
                print('1. Yeah! Database Connected..')
            else:
                print('nope discard')
       except:
            print('terminal error occured')

    def createTable(self):
        try:
            self.mycursor=self.mydb.cursor()
            self.mycursor.execute(''' create table if not exists zx10r(id int auto_increment primary key,notes varchar(150))''')
            print('2. Table Connected Successfully')
            self.mydb.commit()
        except:
            print('table creation terminal error')  

    def addtodo(self):
          try:  
            mycursor=self.mydb.cursor()
            self.viewtask.clear()
            note=self.inputbox.text().strip()
            if (note!=''):
              mycursor.execute(' insert into zx10r(notes) values (%s)',(note,))
              print('3. Data inserted Successfully')
              self.mydb.commit()
              self.inputbox.clear()
              self.viewtodo()
            else:
              self.viewtodo()
              QMessageBox.warning(self, 'Warning','Empty Space not allowed.')
              
          except:
              print('insert terminal error')
              
    def updatetask(self):
        try:
            mycursor=self.mydb.cursor()
            selected=self.viewtask.currentItem()
            if selected:
             selected_id=selected.text().split(':')[0]
             new_note,ok = QInputDialog.getText(self, 'Update Task', 'New Task Description:')
             if ok and new_note !='':
                    mycursor.execute('update zx10r set notes=%s where id=%s',(new_note,selected_id,))
                    print('5. updated Successfully')
                    self.mydb.commit()
                    self.viewtask.clear()
                    self.viewtodo()
             else:
                QMessageBox.warning(self,'warning','empty field not allowed.')
            else:
                QMessageBox.warning(self,'warning','Select item please.')
        except:
            print('update terminal error')
            
    def viewtodo(self):
        try:
            mycursor=self.mydb.cursor(dictionary=True)
            mycursor.execute('select * from zx10r')
            datas=mycursor.fetchall()
            for task in datas:
                    self.viewtask.addItem(f'{task["id"]}: {task["notes"]}')
            print('4. View datas successfully ')
        except:
            print('view terminal error')
    
    def deletetask(self):
        try:  
            mycursor=self.mydb.cursor()
            selected= self.viewtask.currentItem()
            selected_id=selected.text().split(':')[0]
            mycursor.execute(' delete from zx10r where id=%s',(selected_id,))
            print('3. Data Deleted Successfully')
            self.mydb.commit()
            self.viewtask.clear()
            self.viewtodo()
        except:
              QMessageBox.warning(self,'warning','please, Select task from Todo list.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_app=Todo()
    todo_app.show()
    sys.exit(app.exec_())
