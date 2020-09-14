# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search.ui'
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


class Ui_Search(object):
    def setupUi(self, Search):
        if not Search.objectName():
            Search.setObjectName(u"Search")
        Search.resize(400, 600)
        Search.setMinimumSize(QSize(400, 600))
        self.gridLayout = QGridLayout(Search)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.searchLine = QLineEdit(Search)
        self.searchLine.setObjectName(u"searchLine")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchLine.sizePolicy().hasHeightForWidth())
        self.searchLine.setSizePolicy(sizePolicy)
        self.searchLine.setMinimumSize(QSize(50, 0))
        self.searchLine.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.searchLine)

        self.comboBox = QComboBox(Search)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.doButton = QPushButton(Search)
        self.doButton.setObjectName(u"doButton")
        sizePolicy.setHeightForWidth(self.doButton.sizePolicy().hasHeightForWidth())
        self.doButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.doButton)

        self.comboToDo = QComboBox(Search)
        self.comboToDo.addItem("")
        self.comboToDo.addItem("")
        self.comboToDo.addItem("")
        self.comboToDo.setObjectName(u"comboToDo")

        self.horizontalLayout_2.addWidget(self.comboToDo)


        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)

        self.resultList = QListWidget(Search)
        self.resultList.setObjectName(u"resultList")
        font = QFont()
        font.setPointSize(11)
        self.resultList.setFont(font)

        self.gridLayout.addWidget(self.resultList, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.backButton = QPushButton(Search)
        self.backButton.setObjectName(u"backButton")

        self.horizontalLayout_3.addWidget(self.backButton)

        self.tosearchButton = QPushButton(Search)
        self.tosearchButton.setObjectName(u"tosearchButton")

        self.horizontalLayout_3.addWidget(self.tosearchButton)


        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)


        self.retranslateUi(Search)

        QMetaObject.connectSlotsByName(Search)
    # setupUi

    def retranslateUi(self, Search):
        Search.setWindowTitle(QCoreApplication.translate("Search", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Search", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Search", u"\u041c\u043e\u0434\u0435\u0440\u0430\u0442\u043e\u0440", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Search", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))

        self.doButton.setText(QCoreApplication.translate("Search", u"\u0421\u0434\u0435\u043b\u0430\u0442\u044c", None))
        self.comboToDo.setItemText(0, QCoreApplication.translate("Search", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u043c", None))
        self.comboToDo.setItemText(1, QCoreApplication.translate("Search", u"\u041c\u043e\u0434\u0435\u0440\u0430\u0442\u043e\u0440\u043e\u043c", None))
        self.comboToDo.setItemText(2, QCoreApplication.translate("Search", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u043e\u043c", None))

        self.backButton.setText(QCoreApplication.translate("Search", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.tosearchButton.setText(QCoreApplication.translate("Search", u"\u0418\u0441\u043a\u0430\u0442\u044c", None))
    # retranslateUi

