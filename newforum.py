from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
import sys

import mysql.connector
import newforum_ui

class newforum(QtWidgets.QWidget):

    def __init__(self, cnx, main, parent=None):
        super(newforum, self).__init__(parent)

        self.parent = main
        self.cnx = cnx

        self.ui = newforum_ui.Ui_Form()
        self.ui.setupUi(self)

        self.setWindowFlags(self.windowFlags() &\
                            ~QtCore.Qt.WindowCloseButtonHint)

        self.ui.createSection.clicked.connect(self.sectionCreation)
        self.ui.createForumButton.clicked.connect(self.forumCreation)
        self.ui.back.clicked.connect(self.hideWid)

    def forumCreation(self):
        forTitle = self.ui.newForumName.text()
        cursor = self.cnx.cursor()
        cursor.execute(f"INSERT INTO forums (Title) VALUES ('{forTitle}')") 
        self.cnx.commit()
        cursor.close()
        self.hideWid()


    def sectionCreation(self):
        secTitle = self.ui.newSectionName.text()
        parentId = self.parentForumNameId[self.ui.parentForumsList.currentItem().text()]
        cursor = self.cnx.cursor()
        cursor.execute(f"INSERT INTO sections (Title, Forum_id) VALUES ('{secTitle}',{parentId})") 
        self.cnx.commit()
        cursor.close()
        self.hideWid()


    def showW(self):
        self.ui.newForumName.clear()
        self.ui.newSectionName.clear()
        self.ui.parentForumsList.clear()
        self.parentForumNameId = dict()
        cursor = self.cnx.cursor()
        cursor.execute("SELECT Id, Title FROM forums")
        for n, i in enumerate(cursor.fetchall()):
            self.ui.parentForumsList.insertItem(n, i[1])
            self.parentForumNameId[i[1]] = i[0]
        cursor.close()
        self.ui.parentForumsList.setCurrentRow(0)
        self.show()

    def hideWid(self):
        self.hide()
        self.parent.mainWid.fillForum()