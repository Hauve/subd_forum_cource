# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_mainWidget(object):
    def setupUi(self, mainWidget):
        if not mainWidget.objectName():
            mainWidget.setObjectName(u"mainWidget")
        mainWidget.resize(789, 600)
        self.gridLayout = QGridLayout(mainWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.deleteMessage = QPushButton(mainWidget)
        self.deleteMessage.setObjectName(u"deleteMessage")

        self.horizontalLayout.addWidget(self.deleteMessage)

        self.searchButton = QPushButton(mainWidget)
        self.searchButton.setObjectName(u"searchButton")

        self.horizontalLayout.addWidget(self.searchButton)

        self.createTopicButton = QPushButton(mainWidget)
        self.createTopicButton.setObjectName(u"createTopicButton")

        self.horizontalLayout.addWidget(self.createTopicButton)

        self.inButton = QPushButton(mainWidget)
        self.inButton.setObjectName(u"inButton")

        self.horizontalLayout.addWidget(self.inButton)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.tabWidget = QTabWidget(mainWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.forumsSections = QWidget()
        self.forumsSections.setObjectName(u"forumsSections")
        self.gridLayout_3 = QGridLayout(self.forumsSections)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_5 = QLabel(self.forumsSections)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)

        self.gridLayout_4.addWidget(self.label_5, 5, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.forumsSections)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_4.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.sectionCountLabel = QLabel(self.forumsSections)
        self.sectionCountLabel.setObjectName(u"sectionCountLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sectionCountLabel.sizePolicy().hasHeightForWidth())
        self.sectionCountLabel.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.sectionCountLabel)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.forumNameLabel = QLabel(self.forumsSections)
        self.forumNameLabel.setObjectName(u"forumNameLabel")
        font2 = QFont()
        font2.setPointSize(16)
        self.forumNameLabel.setFont(font2)

        self.gridLayout_4.addWidget(self.forumNameLabel, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_4)

        self.sectionList = QListWidget(self.forumsSections)
        self.sectionList.setObjectName(u"sectionList")
        font3 = QFont()
        font3.setPointSize(12)
        self.sectionList.setFont(font3)

        self.verticalLayout_2.addWidget(self.sectionList)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.deleteForumButton = QPushButton(self.forumsSections)
        self.deleteForumButton.setObjectName(u"deleteForumButton")

        self.horizontalLayout_2.addWidget(self.deleteForumButton)

        self.deleteSectionButton = QPushButton(self.forumsSections)
        self.deleteSectionButton.setObjectName(u"deleteSectionButton")

        self.horizontalLayout_2.addWidget(self.deleteSectionButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.forumsSections)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.verticalLayout.addWidget(self.label)

        self.forumList = QListWidget(self.forumsSections)
        self.forumList.setObjectName(u"forumList")
        self.forumList.setFont(font3)

        self.verticalLayout.addWidget(self.forumList)

        self.forumCreate = QPushButton(self.forumsSections)
        self.forumCreate.setObjectName(u"forumCreate")

        self.verticalLayout.addWidget(self.forumCreate)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.forumsSections, "")
        self.topics = QWidget()
        self.topics.setObjectName(u"topics")
        self.gridLayout_5 = QGridLayout(self.topics)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.topicTable = QTableWidget(self.topics)
        if (self.topicTable.columnCount() < 2):
            self.topicTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.topicTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.topicTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.topicTable.setObjectName(u"topicTable")
        self.topicTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.topicTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.topicTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.topicTable.horizontalHeader().setDefaultSectionSize(200)

        self.gridLayout_5.addWidget(self.topicTable, 0, 0, 1, 1)

        self.tabWidget.addTab(self.topics, "")
        self.messages = QWidget()
        self.messages.setObjectName(u"messages")
        self.gridLayout_2 = QGridLayout(self.messages)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.messageTable = QTableWidget(self.messages)
        if (self.messageTable.columnCount() < 3):
            self.messageTable.setColumnCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.messageTable.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.messageTable.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.messageTable.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        self.messageTable.setObjectName(u"messageTable")
        self.messageTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.messageTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.messageTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.messageTable.horizontalHeader().setDefaultSectionSize(200)

        self.gridLayout_2.addWidget(self.messageTable, 0, 0, 1, 1)

        self.messageEdit = QTextEdit(self.messages)
        self.messageEdit.setObjectName(u"messageEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.messageEdit.sizePolicy().hasHeightForWidth())
        self.messageEdit.setSizePolicy(sizePolicy2)
        self.messageEdit.setMaximumSize(QSize(16777215, 150))
        self.messageEdit.setOverwriteMode(False)

        self.gridLayout_2.addWidget(self.messageEdit, 1, 0, 1, 1)

        self.tabWidget.addTab(self.messages, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(mainWidget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWidget)
    # setupUi

    def retranslateUi(self, mainWidget):
        mainWidget.setWindowTitle(QCoreApplication.translate("mainWidget", u"Form", None))
        self.deleteMessage.setText(QCoreApplication.translate("mainWidget", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.searchButton.setText(QCoreApplication.translate("mainWidget", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u0440\u0438\u0432\u0438\u043b\u0435\u0433\u0438\u0439", None))
        self.createTopicButton.setText(QCoreApplication.translate("mainWidget", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0442\u0435\u043c\u0443", None))
        self.inButton.setText(QCoreApplication.translate("mainWidget", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.label_5.setText(QCoreApplication.translate("mainWidget", u"\u0420\u0430\u0437\u0434\u0435\u043b\u044b \u0444\u043e\u0440\u0443\u043c\u0430:", None))
        self.label_4.setText(QCoreApplication.translate("mainWidget", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u043e\u0432:", None))
        self.sectionCountLabel.setText(QCoreApplication.translate("mainWidget", u"TextLabel", None))
        self.forumNameLabel.setText(QCoreApplication.translate("mainWidget", u"ForumName", None))
        self.deleteForumButton.setText(QCoreApplication.translate("mainWidget", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u0439 \u0444\u043e\u0440\u0443\u043c", None))
        self.deleteSectionButton.setText(QCoreApplication.translate("mainWidget", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u0439 \u0440\u0430\u0437\u0434\u0435\u043b", None))
        self.label.setText(QCoreApplication.translate("mainWidget", u"\u0424\u043e\u0440\u0443\u043c\u044b", None))
        self.forumCreate.setText(QCoreApplication.translate("mainWidget", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0444\u043e\u0440\u0443\u043c \u0438\u043b\u0438 \u0440\u0430\u0437\u0434\u0435\u043b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.forumsSections), QCoreApplication.translate("mainWidget", u"\u0424\u043e\u0440\u0443\u043c\u044b \u0438 \u0440\u0430\u0437\u0434\u0435\u043b\u044b", None))
        ___qtablewidgetitem = self.topicTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mainWidget", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem1 = self.topicTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mainWidget", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.topics), QCoreApplication.translate("mainWidget", u"\u0422\u0435\u043c\u044b", None))
        ___qtablewidgetitem2 = self.messageTable.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("mainWidget", u"\u0422\u0435\u043a\u0441\u0442 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem3 = self.messageTable.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("mainWidget", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem4 = self.messageTable.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("mainWidget", u"\u0410\u0432\u0442\u043e\u0440", None));
        self.messageEdit.setHtml(QCoreApplication.translate("mainWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.messages), QCoreApplication.translate("mainWidget", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f", None))
    # retranslateUi

