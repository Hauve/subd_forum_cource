import sys
from PySide2 import QtCore, QtWidgets, QtGui

from auth import Auth
from mainWidget import mainWidget
import mainwidget_ui
import search

import mysql.connector

# Для работы данной программы нужно установить:
# pip install pyside2
# pip install mysql-connector-python
# Далее нужно запустить данный файл с помощью python

# В папке приложения находится файл с расширением .sql (forumDB.sql)
# Код из файла нужно выполнить для базы, чтобы создать нужную структуру бд


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        try:
            self.cnx=mysql.connector.connect(
                user='root', # Имя пользователя настроенное на сервере бд
                password='17932486', # Пароль данного пользователя
                host="localhost", # Сервер. В данном случае локальный
                port= 3306, # Порт. По умолчанию 3306
                database='forumbase') # Название нужной базы на сервере бд
        except Exception as err:
            print(err.args)
            self.cnx = None
        print(self.cnx)
        # end db and ssh init

        self.setMinimumSize(300, 200)
        self.setMaximumSize(300, 200)

        self.AuthWindow = Auth(self.cnx, self)
        self.AuthWindow.show()

        self.mainWid = mainWidget(self.cnx, self)



    def showAppWindow(self):
        self.setMinimumSize(1280, 720)
        self.setMaximumSize(1440, 900)
        self.mainWid.show()
        
        if self.userRole != 'admin' and self.userRole != 'moderator':
            self.mainWid.ui.deleteMessage.setDisabled(True)
            self.mainWid.ui.deleteSectionButton.setDisabled(True)
            self.mainWid.ui.deleteForumButton.setDisabled(True)
            self.mainWid.ui.forumCreate.setDisabled(True)
            self.mainWid.ui.searchButton.setDisabled(True)

        self.search = search.SearchWidget(self.cnx, self)


    def resizeEvent(self, e):
        self.AuthWindow.resize(e.size().width(), e.size().height())
        self.mainWid.resize(e.size().width(), e.size().height())


    def searchWid(self):
        if self.search.isHidden():
            self.search.show()
        else: self.search.hide()


    def __del__(self):
        self.cnx.close()
        self.server.stop()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
