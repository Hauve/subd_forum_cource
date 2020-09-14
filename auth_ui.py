# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'authwindow.ui'
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


class Ui_Auth(object):
    def setupUi(self, Auth):
        if not Auth.objectName():
            Auth.setObjectName(u"Auth")
        Auth.resize(300, 200)
        self.gridLayout = QGridLayout(Auth)
        self.gridLayout.setObjectName(u"gridLayout")
        self.errLabel = QLabel(Auth)
        self.errLabel.setObjectName(u"errLabel")
        font = QFont()
        font.setPointSize(11)
        self.errLabel.setFont(font)
        self.errLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.errLabel, 2, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label = QLabel(Auth)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.usernameEdit = QLineEdit(Auth)
        self.usernameEdit.setObjectName(u"usernameEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.usernameEdit)

        self.label_2 = QLabel(Auth)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.passEdit = QLineEdit(Auth)
        self.passEdit.setObjectName(u"passEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.passEdit)

        self.registerPushButton = QPushButton(Auth)
        self.registerPushButton.setObjectName(u"registerPushButton")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.registerPushButton)

        self.loginPushButton = QPushButton(Auth)
        self.loginPushButton.setObjectName(u"loginPushButton")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.loginPushButton)


        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)


        self.retranslateUi(Auth)

        QMetaObject.connectSlotsByName(Auth)
    # setupUi

    def retranslateUi(self, Auth):
        Auth.setWindowTitle(QCoreApplication.translate("Auth", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.errLabel.setText("")
        self.label.setText(QCoreApplication.translate("Auth", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Auth", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.registerPushButton.setText(QCoreApplication.translate("Auth", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.loginPushButton.setText(QCoreApplication.translate("Auth", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

