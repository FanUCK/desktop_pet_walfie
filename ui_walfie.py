# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:/codemao_py/desktop_pet_walfie/walfie.ui',
# licensing of 'F:/codemao_py/desktop_pet_walfie/walfie.ui' applies.
#
# Created: Thu Feb  4 10:15:42 2021
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Walfie(object):
    def setupUi(self, Walfie):
        Walfie.setObjectName("Walfie")
        Walfie.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Walfie)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        Walfie.setCentralWidget(self.centralwidget)

        self.retranslateUi(Walfie)
        QtCore.QMetaObject.connectSlotsByName(Walfie)

    def retranslateUi(self, Walfie):
        Walfie.setWindowTitle(QtWidgets.QApplication.translate("Walfie", "Walfie", None, -1))

