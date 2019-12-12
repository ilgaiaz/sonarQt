# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sonar.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


class Ui_Sonarmapping(object):
    def __init__(self):
        super().__init__()
        self.dlg = QtWidgets.QMainWindow()
        self.setupUi(self.dlg)
        self.dlg.show()

    def setupUi(self, Sonarmapping):
        Sonarmapping.setObjectName("Sonarmapping")
        Sonarmapping.resize(416, 297)
        self.centralwidget = QtWidgets.QWidget(Sonarmapping)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(50, 20, 301, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 189, 311, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        Sonarmapping.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Sonarmapping)
        self.statusbar.setObjectName("statusbar")
        Sonarmapping.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(Sonarmapping)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(Sonarmapping)
        QtCore.QMetaObject.connectSlotsByName(Sonarmapping)

    def retranslateUi(self, Sonarmapping):
        _translate = QtCore.QCoreApplication.translate
        Sonarmapping.setWindowTitle(_translate("Sonarmapping", "MainWindow"))
        self.label.setText(_translate("Sonarmapping", "Connessione :"))
        self.pushButton_2.setText(_translate("Sonarmapping", "Connection"))
        self.pushButton.setText(_translate("Sonarmapping", "Start mapping"))
        self.actionExit.setText(_translate("Sonarmapping", "Exit"))

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    dlg = Ui_Sonarmapping()
    
    sys.exit(app.exec_())