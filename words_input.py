# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'words_input.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(897, 622)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 901, 621))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/testing_back.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(330, 230, 47, 13))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(300, 230, 391, 31))
        self.label_5.setStyleSheet("font: 16pt \"MS Sans Serif\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(300, 160, 261, 51))
        self.label_6.setStyleSheet("font: 16pt \"MS Sans Serif\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(300, 260, 451, 31))
        self.label_7.setStyleSheet("font: 16pt \"MS Sans Serif\";")
        self.label_7.setObjectName("label_7")
        self.translation_input = QtWidgets.QLineEdit(Dialog)
        self.translation_input.setGeometry(QtCore.QRect(300, 390, 371, 61))
        self.translation_input.setObjectName("translation_input")
        self.word_input = QtWidgets.QLineEdit(Dialog)
        self.word_input.setGeometry(QtCore.QRect(300, 310, 371, 61))
        self.word_input.setStyleSheet("background: transparent\n"
"\n"
"")
        self.word_input.setObjectName("word_input")
        self.ok_button = QtWidgets.QPushButton(Dialog)
        self.ok_button.setGeometry(QtCore.QRect(450, 510, 121, 51))
        self.ok_button.setStyleSheet("background-color:rgb(73, 73, 73, );\n"
"font: 16pt \"MS Sans Serif\";\n"
"border-radius: 10px;\n"
"-moz-border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"font-weight:600")
        self.ok_button.setObjectName("ok_button")
        self.back_button = QtWidgets.QPushButton(Dialog)
        self.back_button.setGeometry(QtCore.QRect(300, 510, 131, 51))
        self.back_button.setStyleSheet("background-color:rgb(255, 255, 255, );\n"
"font: 16pt \"MS Sans Serif\";\n"
"color: rgb(73, 73, 73);\n"
"border-radius: 15px;\n"
"font-weight:600\n"
"")
        self.back_button.setObjectName("back_button")
        self.label_3.raise_()
        self.translation_input.raise_()
        self.word_input.raise_()
        self.ok_button.raise_()
        self.back_button.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "Тут ты можешь добавить слова,которые"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600;\">Новые слова</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "хочешь выучить. Они появятся в тесте"))
        self.translation_input.setText(_translate("Dialog", "Введите перевод"))
        self.word_input.setText(_translate("Dialog", "Введите английское слово"))
        self.ok_button.setText(_translate("Dialog", "Добавить"))
        self.back_button.setText(_translate("Dialog", "На главную"))
