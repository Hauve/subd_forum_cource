from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
import sys

import mysql.connector
import newtopic_ui

class newtopic(QtWidgets.QWidget):

    def __init__(self, cnx, main, parent=None):
        super(newtopic, self).__init__(parent)

        self.parent = main
        self.cnx = cnx

        self.ui = newtopic_ui.Ui_Form()
        self.ui.setupUi(self)

        self.setWindowFlags(self.windowFlags() &\
                            ~QtCore.Qt.WindowCloseButtonHint)

        self.ui.backButton.clicked.connect(self.backPressed)
        self.ui.createButton.clicked.connect(self.createPressed)
    

    def createPressed(self):
        topicName = self.ui.titleEdit.text()
        sectionId = self.dictTitleId[self.ui.sectionsList.currentItem().text()]
        
        textContent = self.ui.initMessageEdit.toPlainText()
        textContent = textContent.split(" ")
        for i in range(len(textContent)):
            if i % 15 == 0 and i != 0:
                textContent[i] = textContent[i] + "\n"
        textContent = " ".join(textContent)
        
        cursor = self.cnx.cursor()
        query = "INSERT INTO topics (Title, Section_id)" +\
            f"VALUES ('{topicName}', {sectionId});"
        cursor.execute(query)
        self.cnx.commit()
        cursor.close()

        cursor = self.cnx.cursor()
        cursor.execute(f'SELECT Id FROM topics WHERE Title = "{topicName}"')
        topicId = cursor.fetchall()

        cursor = self.cnx.cursor()
        query = 'INSERT INTO messages (TextContent, Author, Topic_id) VALUES ("'+textContent+'", '+str(self.parent.userId)+', '+str(topicId[0][0])+')'
        cursor.execute(query)
        self.cnx.commit()
        cursor.close()
        self.hide()
        self.parent.mainWid.ui.tabWidget.setCurrentIndex(0)


    def showWid(self):
        self.ui.titleEdit.clear()
        self.ui.sectionsList.clear()
        self.ui.initMessageEdit.clear()
        self.show()
        cursor = self.cnx.cursor()
        self.dictTitleId = dict()
        cursor.execute("SELECT * FROM sections")
        for n, i in enumerate(cursor.fetchall()):
            self.ui.sectionsList.insertItem(n, i[1])
            self.dictTitleId[i[1]] = i[0]
        cursor.close()
        self.ui.sectionsList.setCurrentRow(0)


    def backPressed(self):
        self.ui.titleEdit.clear()
        self.ui.sectionsList.clear()
        self.ui.initMessageEdit.clear()
        self.hide()