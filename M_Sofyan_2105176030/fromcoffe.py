# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fromcoffe.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import image_rc, sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(899, 451)
        Form.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.horizontalFrame = QtWidgets.QFrame(Form)
        self.horizontalFrame.setGeometry(QtCore.QRect(300, 50, 308, 101))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalFrame)
        self.label.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_7 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_7.setStyleSheet("image:url(:/img/download (1).jpeg);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_2 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_2.setStyleSheet("font: 75 40pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(300, 210, 311, 41))
        self.lineEdit.setStyleSheet("border:none;\n"
"border-bottom:1px solid;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 270, 311, 31))
        self.lineEdit_2.setStyleSheet("border:none;\n"
"border-bottom:1px solid;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(300, 320, 311, 41))
        self.lineEdit_3.setStyleSheet("border:none;\n"
"border-bottom:1px solid;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(300, 160, 311, 41))
        self.label_3.setStyleSheet("border:0;\n"
"border-bottom:1px solid;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(620, 150, 271, 221))
        self.label_4.setStyleSheet("image:url(:/img/download (1).jpeg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 271, 181))
        self.label_6.setStyleSheet("image:url(:/img/download (2).jpeg)")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(300, 380, 75, 23))
        self.pushButton.setStyleSheet("background-color:rgb(0, 255, 0)")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(440, 380, 171, 16))
        self.label_5.setStyleSheet("color :rgb(255, 0, 0)")
        self.label_5.setObjectName("label_5")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 0, 881, 441))
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.label_6.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label_5.raise_()
        self.pushButton.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.lineEdit_3.raise_()
        self.horizontalFrame.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "SUKA-SUKA"))
        self.label_2.setText(_translate("Form", "KOPI"))
        self.lineEdit.setText(_translate("Form", "NAMA "))
        self.lineEdit_2.setText(_translate("Form", "PESANAN"))
        self.lineEdit_3.setText(_translate("Form", "NO.WA"))
        self.label_3.setText(_translate("Form", "By : M.Sofyan"))
        self.pushButton.setText(_translate("Form", "PESAN"))
        self.label_5.setText(_translate("Form", "LIAT PESANAN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
