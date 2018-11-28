# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/home.ui'
#
# Created: Tue Nov 20 18:11:14 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(536, 231)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(Form)
        self.widget.setStyleSheet("background:#FF6E00;\n"
"color:#fff;")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("A Jannat LT")
        font.setPointSize(28)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet("background:#1E252F;\n"
"color:#FF6E00;")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("A Jannat LT")
        font.setPointSize(28)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "مشغل الصوت", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "عميل رقم 5 شباك رقم 10", None, QtGui.QApplication.UnicodeUTF8))

