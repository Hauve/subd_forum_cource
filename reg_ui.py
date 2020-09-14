# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'regwindow.ui'
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


class Ui_RegWindow(object):
    def setupUi(self, RegWindow):
        if not RegWindow.objectName():
            RegWindow.setObjectName(u"RegWindow")
        RegWindow.resize(400, 290)
        self.gridLayout = QGridLayout(RegWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label = QLabel(RegWindow)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_name = QLineEdit(RegWindow)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_name)

        self.label_2 = QLabel(RegWindow)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_2_pass = QLineEdit(RegWindow)
        self.lineEdit_2_pass.setObjectName(u"lineEdit_2_pass")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2_pass)

        self.label_3 = QLabel(RegWindow)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_3_repass = QLineEdit(RegWindow)
        self.lineEdit_3_repass.setObjectName(u"lineEdit_3_repass")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3_repass)

        self.pushButton_reg = QPushButton(RegWindow)
        self.pushButton_reg.setObjectName(u"pushButton_reg")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.pushButton_reg)

        self.pushButton_2_cancel = QPushButton(RegWindow)
        self.pushButton_2_cancel.setObjectName(u"pushButton_2_cancel")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.pushButton_2_cancel)


        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)

        self.errLabel = QLabel(RegWindow)
        self.errLabel.setObjectName(u"errLabel")
        font = QFont()
        font.setPointSize(11)
        self.errLabel.setFont(font)
        self.errLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.errLabel, 2, 0, 1, 1)

        self.textBrowser = QTextBrowser(RegWindow)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 0, 1, 1)


        self.retranslateUi(RegWindow)

        QMetaObject.connectSlotsByName(RegWindow)
    # setupUi

    def retranslateUi(self, RegWindow):
        RegWindow.setWindowTitle(QCoreApplication.translate("RegWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("RegWindow", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_2.setText(QCoreApplication.translate("RegWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_3.setText(QCoreApplication.translate("RegWindow", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButton_reg.setText(QCoreApplication.translate("RegWindow", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.pushButton_2_cancel.setText(QCoreApplication.translate("RegWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.errLabel.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("RegWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0412 \u0438\u043c\u0435\u043d\u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f \u0438 \u0432 \u043f\u0430\u0440\u043e\u043b\u0435 \u043c\u043e\u0433\u0443\u0442 \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0442\u044c\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u043b\u0430\u0442\u0438\u043d\u0441\u043a\u0438\u0435 \u0431\u0443\u043a\u0432\u044b, \u0446\u0438\u0444\u0440\u044b \u0438 \u0437\u043d\u0430\u043a\u0438 \u043f\u043e\u0434\u0447\u0451\u0440\u043a\u0438\u0432\u0430"
                        "\u043d\u0438\u044f. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0434\u043b\u0438\u043d\u0430 \u0438\u043c\u0435\u043d\u0438 - 5 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432, \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f - 20.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0434\u043b\u0438\u043d\u0430 \u043f\u0430\u0440\u043e\u043b\u044f - 8 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432, \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f - 20.<br />\u0420\u0435\u0433\u0438\u0441\u0442\u0440 \u0438\u043c\u0435\u043d\u0438 \u043d\u0435 \u0438\u043c"
                        "\u0435\u0435\u0442 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f.</span></p></body></html>", None))
    # retranslateUi

