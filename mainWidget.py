from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
import sys

import mysql.connector
import mainwidget_ui
import newtopic
import newforum

class mainWidget(QtWidgets.QWidget):

    def __init__(self, cnx, parent=None):
        super(mainWidget, self).__init__(parent)

        self.parent = parent
        self.cnx = cnx

        self.ui = mainwidget_ui.Ui_mainWidget()
        self.ui.setupUi(self)

        parent.setWindowTitle("Cyberfor")
        self.hide()
        # self.ui.forumTable.currentItemChanged.connect(self.setSection)
        # self.ui.sectionTable.currentItemChanged.connect(self.setTopics)
        # self.ui.topicTable.currentItemChanged.connect(self.setMessages)
        self.ui.forumList.currentRowChanged.connect(self.forumRowChanged)
        self.ui.inButton.clicked.connect(self.inFunction)

        self.ui.searchButton.clicked.connect(self.parent.searchWid)
        self.ui.createTopicButton.clicked.connect(self.toCreateTopic)
        self.ui.forumCreate.clicked.connect(self.createForum)
        self.ui.deleteForumButton.clicked.connect(self.deleteCurrentForum)
        self.ui.deleteSectionButton.clicked.connect(self.deleteCurrentSection)

        self.ui.deleteMessage.clicked.connect(self.removeMessage)

        self.topicCreator = newtopic.newtopic(self.cnx, self.parent)
        self.forumCreator = newforum.newforum(self.cnx, self.parent)

        self.fillForum()

    def removeMessage(self):
        try:
            textMessage = self.ui.messageTable.currentItem().text()
            cursor = self.cnx.cursor()
            cursor.execute(f"DELETE FROM messages WHERE TextContent = '{textMessage}'")
            self.cnx.commit()
            cursor.close()
            self.ui.tabWidget.setCurrentIndex(1)
            self.inFunction()
        except Exception as err:
            print(err.args)


    def deleteCurrentSection(self):
        try:
            titleSection = self.ui.sectionList.currentItem().text()
            cursor = self.cnx.cursor()
            cursor.execute(f"DELETE FROM sections WHERE Title = '{titleSection}'")
            self.cnx.commit()
            cursor.close()
            self.fillForum()
        except Exception as err:
            print(err.args)


    def deleteCurrentForum(self):
        try:
            titleForum = self.ui.forumList.currentItem().text()
            cursor = self.cnx.cursor()
            cursor.execute(f"DELETE FROM forums WHERE Title = '{titleForum}'")
            self.cnx.commit()
            cursor.close()
            self.fillForum()
        except Exception as err:
            print(err.args)


    def createForum(self):
        self.forumCreator.showW()

    def toCreateTopic(self):
        self.topicCreator.ui.titleEdit.clear()
        self.topicCreator.ui.sectionsList.clear()
        self.topicCreator.showWid()

    def fillForum(self):
        try:
            self.ui.forumList.clear()
            
            self.ui.tabWidget.setTabEnabled(0, True)
            self.ui.tabWidget.setTabEnabled(1, False)
            self.ui.tabWidget.setTabEnabled(2, False)
            self.forumList = []
            cursor = self.cnx.cursor()
            cursor.execute("SELECT * FROM forums ORDER BY Id")
            for tuple_i in cursor.fetchall():
                # print(tuple_i)
                self.ui.forumList.addItem(tuple_i[1])    
                self.forumList.append(tuple_i)  
            self.ui.forumList.setCurrentRow(0)
            cursor.close()
            self.ui.tabWidget.currentChanged.connect(self.tabChanged)
        except Exception as err:
            print(err.args)


    def forumRowChanged(self, currentRow):
        try:
            self.ui.sectionList.clear()
            self.ui.tabWidget.setTabEnabled(0, True)
            self.ui.tabWidget.setTabEnabled(1, False)
            self.ui.tabWidget.setTabEnabled(2, False)

            self.selectedForum = self.forumList[currentRow]
            currentId = self.selectedForum[0]

            self.sectionList = []
            sectionCounter = 0
            cursor = self.cnx.cursor()
            cursor.execute(f"SELECT * FROM sections WHERE Forum_id = {currentId}")
            for tuple_i in cursor.fetchall():
                # print(tuple_i)
                self.ui.sectionList.addItem(tuple_i[1])    
                self.sectionList.append(tuple_i)
                sectionCounter = sectionCounter + 1
            self.ui.forumNameLabel.setText(self.selectedForum[1])
            self.ui.sectionCountLabel.setText(str(sectionCounter))
            self.ui.sectionList.setCurrentRow(0)
            cursor.close()
        except Exception as err:
            print(err.args)

    def inFunction(self):
        try:
            if self.ui.tabWidget.currentIndex() == 0:
                if self.ui.sectionList.currentRow() == -1:
                    return
                self.selectedSection = self.sectionList[self.ui.sectionList.currentRow()]
                self.ui.tabWidget.setTabEnabled(0, True)
                self.ui.tabWidget.setTabEnabled(1, True)
                self.ui.tabWidget.setTabEnabled(2, False)
                self.ui.tabWidget.setCurrentIndex(1)
                self.ui.topicTable.setRowCount(0)
                
                currentId = self.selectedSection[0]
                self.topicList = []
                cursor = self.cnx.cursor()
                cursor.execute(f"SELECT * FROM topics WHERE Section_id = {currentId} ORDER BY Dt_last_mes")
                counter_row = 0
                for tuple_i in cursor.fetchall():
                    self.ui.topicTable.setRowCount(counter_row+1)
                    self.ui.topicTable.setItem(counter_row, 0, QTableWidgetItem(tuple_i[1]))
                    self.ui.topicTable.setItem(counter_row, 1, QTableWidgetItem(str(tuple_i[2])))
                    # print(tuple_i)
                    self.topicList.append(tuple_i)
                    counter_row = counter_row + 1
                if counter_row > 0:
                    self.ui.topicTable.resizeColumnsToContents()

                cursor.close()
                self.ui.topicTable.setCurrentCell(0, 0)

            elif self.ui.tabWidget.currentIndex() == 1:
                if self.ui.topicTable.currentRow() == -1:
                    return
                self.selectedTopic = self.topicList[self.ui.topicTable.currentRow()]
                self.ui.tabWidget.setTabEnabled(0, True)
                self.ui.tabWidget.setTabEnabled(1, True)
                self.ui.tabWidget.setTabEnabled(2, True)
                self.ui.tabWidget.setCurrentIndex(2)
                self.ui.messageTable.setRowCount(0)

                currentId = self.selectedTopic[0]
                self.messageList = []
                cursor = self.cnx.cursor()
                cursor.execute(f"SELECT * FROM messages WHERE Topic_id = {currentId} ORDER BY Create_dt")
                counter_row = 0
                for tuple_i in cursor.fetchall():
                    self.ui.messageTable.setRowCount(counter_row+1)
                    self.ui.messageTable.setItem(counter_row, 0, QTableWidgetItem(tuple_i[1]))
                    self.ui.messageTable.setItem(counter_row, 1, QTableWidgetItem(str(tuple_i[2])))
                    self.messageList.append(tuple_i)
                    counter_row = counter_row + 1
                cursor.close()

                Id = [i[3] for i in self.messageList]
                dictID = dict()
                author_id = set(Id)
                for i in author_id:
                    cursor = self.cnx.cursor()
                    cursor.execute(f"SELECT Username FROM users WHERE Id = {i}")
                    for tuple_i in cursor.fetchall():
                        dictID[i] = tuple_i[0]
                    cursor.close()
                for i, z in enumerate(Id):
                    self.ui.messageTable.setItem(i, 2, QTableWidgetItem(dictID[z]))

                if counter_row > 0:
                    self.ui.messageTable.resizeColumnsToContents()
                    self.ui.messageTable.resizeRowsToContents()

            elif self.ui.tabWidget.currentIndex() == 2:
                text = self.ui.messageEdit.toPlainText()
                text = text.split(" ")
                for i in range(len(text)):
                    if i % 15 == 0 and i != 0:
                        text[i] = text[i] + "\n"
                text = " ".join(text)
                print(text)
                self.ui.messageEdit.clear()
            
                cursor = self.cnx.cursor()
                cursor.execute('INSERT INTO messages (TextContent, Author, Topic_id) VALUES ("'+\
                                text + '", ' + str(self.parent.userId) + ', ' + str(self.selectedTopic[0])+ ')')
                self.cnx.commit()
                cursor.close()

                cursor = self.cnx.cursor()
                cursor.execute(f"SELECT Create_dt FROM messages WHERE Author = {self.parent.userId}")
                rowCount = self.ui.messageTable.rowCount()
                for i in cursor.fetchall():
                    self.ui.messageTable.setRowCount(rowCount+1)
                    self.ui.messageTable.setItem(rowCount, 0, QTableWidgetItem(str(text)))
                    self.ui.messageTable.setItem(rowCount, 1, QTableWidgetItem(str(i[0])))
                    self.ui.messageTable.setItem(rowCount, 2, QTableWidgetItem(self.parent.userName))
                    self.ui.messageTable.resizeColumnsToContents()
                    self.ui.messageTable.resizeRowsToContents()
                    break
        except Exception as err:
            print(err.args)


    
    def tabChanged(self, currentTab):
        if currentTab == 2:
            self.ui.inButton.setText("Ответить")
        else:
            self.ui.inButton.setText("Войти")
