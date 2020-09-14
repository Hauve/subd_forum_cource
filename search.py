from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
import sys

import mysql.connector
import search_ui

class SearchWidget(QtWidgets.QWidget):

    def __init__(self, cnx, main, parent=None):
        super(SearchWidget, self).__init__(parent)

        self.cnx = cnx
        self.parent = main

        self.ui = search_ui.Ui_Search()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() &\
                            ~QtCore.Qt.WindowCloseButtonHint)
        self.ui.backButton.clicked.connect(self.backPressed)
        self.ui.tosearchButton.clicked.connect(self.searchPressed)
        self.ui.doButton.clicked.connect(self.doPressed)


    def doPressed(self):
        resultText = self.ui.resultList.currentItem().text()
        comboText = self.ui.comboToDo.currentText()
        if comboText == "Администратором":
            typeRole = "admin"
        elif comboText == "Модератором":
            typeRole = "moderator"
        elif comboText == "Пользователем":
            typeRole = "client"
        if self.users[resultText] == typeRole:
            self.ui.doButton.setText(self.ui.doButton.text()+"(Не удалось)")
            return
        cursor = self.cnx.cursor()
        cursor.execute(f"UPDATE users SET Role = '{typeRole}' "\
            f"WHERE Username = '{resultText}'")
        self.cnx.commit()
        cursor.close()
        self.ui.doButton.setText(self.ui.doButton.text()+"(OK)")


    def searchPressed(self):
        self.ui.resultList.clear()
        self.ui.doButton.setText("Сделать")
        text = self.ui.searchLine.text()
        comboText = self.ui.comboBox.currentText()

        if comboText == "Администратор":
            typeRole = "admin"
        elif comboText == "Модератор":
            typeRole = "moderator"
        elif comboText == "Пользователь":
            typeRole = "client"
        
        cursor = self.cnx.cursor()
        self.users = {}

        cursor.execute(f'SELECT Username, Role FROM users WHERE Role = "{typeRole}"')
        for i in cursor.fetchall():
            print(i)
            if i[0].lower().find(text.lower()) == -1:
                continue
            self.users[i[0]] = i[1]    
            self.ui.resultList.addItem(i[0])


    def backPressed(self):
        self.ui.searchLine.clear()
        self.ui.resultList.clear()
        self.hide()
        