# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'walfie.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Walfie(object):
    def setupUi(self, Walfie):
        if not Walfie.objectName():
            Walfie.setObjectName(u"Walfie")
        Walfie.resize(800, 600)
        self.centralwidget = QWidget(Walfie)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 751, 561))
        Walfie.setCentralWidget(self.centralwidget)

        self.retranslateUi(Walfie)

        QMetaObject.connectSlotsByName(Walfie)
    # setupUi

    def retranslateUi(self, Walfie):
        Walfie.setWindowTitle(QCoreApplication.translate("Walfie", u"Walfie", None))
        self.label.setText("")
    # retranslateUi

