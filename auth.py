from PySide2 import QtCore, QtWidgets, QtGui
import sys

import auth_ui
import reg_ui
import mysql.connector

class Auth(QtWidgets.QWidget):

    def __init__(self, cnx, parent=None):
        super().__init__(parent)

        self.parent = parent
        self.cnx = cnx

        self.ui = auth_ui.Ui_Auth()
        self.ui.setupUi(self)

        self.reg = QtWidgets.QWidget(self.parent)
        self.regUI = reg_ui.Ui_RegWindow()
        self.regUI.setupUi(self.reg)
        self.reg.hide()

        parent.setWindowTitle("Авторизация")

        

        self.ui.loginPushButton.clicked.connect(self.to_login)
        self.ui.registerPushButton.clicked.connect(self.show_reg_ui)



    def show_reg_ui(self):
        print("click")
        self.ui.errLabel.setText("")

        self.parent.setWindowTitle("Регистрация")
        self.parent.setMinimumSize(400, 300)
        self.parent.setMaximumSize(400, 300)
        self.hide()
        self.reg.show()
        
        
        def to_register():
            print("Click reg")
            nameText = self.regUI.lineEdit_name.text()
            passText = self.regUI.lineEdit_2_pass.text()
            repassText = self.regUI.lineEdit_3_repass.text()
            if len(nameText) < 5 or len(nameText) > 20:
                self.regUI.errLabel.setText("Неверная длина имени")
            elif len(passText) < 8 or len(passText) > 20:
                self.regUI.errLabel.setText("Неверная длина пароля")
            elif passText != repassText:
                self.regUI.errLabel.setText("Пароли не совпадают")
            else:
                try:
                    cursor = self.cnx.cursor()
                    cursor.execute("SELECT Id FROM users WHERE Username = \"" + nameText + "\"")
                    for _ in cursor:
                        self.regUI.errLabel.setText("Имя занято")
                        cursor.close()
                        return
                    
                    cursor = self.cnx.cursor()
                    add_user = ("INSERT INTO users "
                        "(Username,Pass,Role) "
                        "VALUES (%s, %s, %s)")
                    data_user = (self.regUI.lineEdit_name.text(),
                                self.regUI.lineEdit_2_pass.text(),
                                "client")
                    cursor.execute(add_user, data_user)
                    self.cnx.commit()
                    cursor.close()
                except Exception as err:
                    print(err.args)
                self.reg.hide()
                self.show()

        def to_cancel():
            self.regUI.lineEdit_name.setText("")
            self.regUI.lineEdit_2_pass.setText("")
            self.regUI.lineEdit_3_repass.setText("")
            self.regUI.errLabel.setText("")

            self.parent.setWindowTitle("Авторизация")
            self.parent.setMinimumSize(300, 200)
            self.parent.setMaximumSize(300, 200)
            self.reg.hide()
            self.show()
        
        self.regUI.pushButton_reg.clicked.connect(to_register)
        self.regUI.pushButton_2_cancel.clicked.connect(to_cancel)


    def to_login(self):
        username = self.ui.usernameEdit.text()
        password = self.ui.passEdit.text()
        if len(username) < 5 or len(username) > 20:
            self.ui.errLabel.setText("Неверное имя пользователя или пароль")
        elif len(password) < 8 or len(password) > 20:
            self.ui.errLabel.setText("Неверное имя пользователя или пароль")
        else:
            try:
                cursor = self.cnx.cursor()
                cursor.execute("SELECT * FROM users WHERE Username = \"%s\" AND Pass = \"%s\""%(username, password))

                row = cursor.fetchone()
                if row is not None:
                    print(row)
                    self.parent.userId = row[0]
                    self.parent.userName = row[1]
                    self.parent.userRole = row[3]

                    self.hide()
                    cursor.close()
                    self.parent.showAppWindow()

                else:
                    cursor.close()
                    self.ui.errLabel.setText("Неверное имя пользователя или пароль")
            except Exception as err:
                print(err.args)
                
            
