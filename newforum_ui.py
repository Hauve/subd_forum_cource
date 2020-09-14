# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createforum.ui'
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


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.newForumName = QLineEdit(Form)
        self.newForumName.setObjectName(u"newForumName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.newForumName)

        self.createForumButton = QPushButton(Form)
        self.createForumButton.setObjectName(u"createForumButton")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.createForumButton)

        self.verticalSpacer = QSpacerItem(20, 300, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(2, QFormLayout.FieldRole, self.verticalSpacer)


        self.verticalLayout.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.newSectionName = QLineEdit(Form)
        self.newSectionName.setObjectName(u"newSectionName")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.newSectionName)

        self.createSection = QPushButton(Form)
        self.createSection.setObjectName(u"createSection")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.createSection)

        self.parentForumsList = QListWidget(Form)
        self.parentForumsList.setObjectName(u"parentForumsList")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.parentForumsList)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.back = QPushButton(Form)
        self.back.setObjectName(u"back")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.back)


        self.verticalLayout.addLayout(self.formLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0438\u043b\u0438 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0444\u043e\u0440\u0443\u043c\u0430", None))
        self.createForumButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u0430", None))
        self.createSection.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0439 \u0444\u043e\u0440\u0443\u043c", None))
        self.back.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

