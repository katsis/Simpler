# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testing.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(897, 673)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 931, 641))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/testing_back.png"))
        self.label.setObjectName("label")
        self.correct_answers_label = QtWidgets.QLabel(self.centralwidget)
        self.correct_answers_label.setGeometry(QtCore.QRect(850, 20, 31, 21))
        self.correct_answers_label.setStyleSheet("font: 16pt \"MS Sans Serif\";\n"
"color: rgb(127,176,105,1)")
        self.correct_answers_label.setObjectName("correct_answers_label")
        self.wrong_answers_label = QtWidgets.QLabel(self.centralwidget)
        self.wrong_answers_label.setGeometry(QtCore.QRect(850, 70, 31, 21))
        self.wrong_answers_label.setStyleSheet("font: 16pt \"MS Sans Serif\";\n"
"color: rgb(227,23,10,1)")
        self.wrong_answers_label.setObjectName("wrong_answers_label")
        self.correct_answers = QtWidgets.QLabel(self.centralwidget)
        self.correct_answers.setGeometry(QtCore.QRect(660, 30, 181, 20))
        self.correct_answers.setStyleSheet("font: 12pt \"MS Sans Serif\";")
        self.correct_answers.setObjectName("correct_answers")
        self.mistakes = QtWidgets.QLabel(self.centralwidget)
        self.mistakes.setGeometry(QtCore.QRect(760, 70, 81, 31))
        self.mistakes.setStyleSheet("font: 12pt \"MS Sans Serif\";")
        self.mistakes.setObjectName("mistakes")
        self.english_word = QtWidgets.QLabel(self.centralwidget)
        self.english_word.setGeometry(QtCore.QRect(300, 270, 297, 31))
        self.english_word.setStyleSheet("font: 16pt \"MS Sans Serif\";\n"
"")
        self.english_word.setObjectName("english_word")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 220, 271, 31))
        self.label_2.setStyleSheet("font: 16pt \"MS Sans Serif\";")
        self.label_2.setObjectName("label_2")
        self.answer_button = QtWidgets.QPushButton(self.centralwidget)
        self.answer_button.setGeometry(QtCore.QRect(300, 510, 161, 51))
        self.answer_button.setStyleSheet("background-color:rgb(73, 73, 73, );\n"
"font: 16pt \"MS Sans Serif\";\n"
"border-radius: 10px;\n"
"-moz-border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"font-weight:600")
        self.answer_button.setObjectName("answer_button")
        self.skip_button = QtWidgets.QPushButton(self.centralwidget)
        self.skip_button.setGeometry(QtCore.QRect(470, 510, 171, 51))
        self.skip_button.setStyleSheet("background-color:rgb(255, 255, 255, );\n"
"font: 16pt \"MS Sans Serif\";\n"
"color: rgb(73, 73, 73);\n"
"border-radius: 15px;\n"
"font-weight:600\n"
"")
        self.skip_button.setObjectName("skip_button")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 160, 261, 51))
        self.label_3.setStyleSheet("font: 16pt \"MS Sans Serif\";")
        self.label_3.setObjectName("label_3")
        self.translation3 = QtWidgets.QRadioButton(self.centralwidget)
        self.translation3.setGeometry(QtCore.QRect(301, 401, 411, 27))
        self.translation3.setStyleSheet("font: 16pt \"MS Sans Serif\";")
        self.translation3.setObjectName("translation3")
        self.translation1 = QtWidgets.QRadioButton(self.centralwidget)
        self.translation1.setGeometry(QtCore.QRect(301, 319, 391, 27))
        self.translation1.setStyleSheet("font: 16pt \"MS Sans Serif\";\n"
"")
        self.translation1.setObjectName("translation1")
        self.translation2 = QtWidgets.QRadioButton(self.centralwidget)
        self.translation2.setGeometry(QtCore.QRect(301, 360, 401, 27))
        self.translation2.setStyleSheet("font: 16pt \"MS Sans Serif\";")
        self.translation2.setObjectName("translation2")
        self.translation4 = QtWidgets.QRadioButton(self.centralwidget)
        self.translation4.setGeometry(QtCore.QRect(301, 442, 411, 27))
        self.translation4.setStyleSheet("font: 16pt \"MS Sans Serif\";")
        self.translation4.setObjectName("translation4")
        self.back_from_testing_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_from_testing_button.setGeometry(QtCore.QRect(290, 130, 171, 31))
        self.back_from_testing_button.setStyleSheet("background-color:rgb(255, 255, 255, );\n"
"font: 16pt \"MS Sans Serif\";\n"
"color: rgb(153, 153, 153);\n"
"border-radius: 15px;\n"
"font-weight:600\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon_arrow.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_from_testing_button.setIcon(icon)
        self.back_from_testing_button.setIconSize(QtCore.QSize(20, 20))
        self.back_from_testing_button.setObjectName("back_from_testing_button")
        self.label.raise_()
        self.answer_button.raise_()
        self.skip_button.raise_()
        self.correct_answers_label.raise_()
        self.wrong_answers_label.raise_()
        self.correct_answers.raise_()
        self.mistakes.raise_()
        self.english_word.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.translation3.raise_()
        self.translation1.raise_()
        self.translation2.raise_()
        self.translation4.raise_()
        self.back_from_testing_button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 897, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.correct_answers_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">0</span></p></body></html>"))
        self.wrong_answers_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">0</span></p></body></html>"))
        self.correct_answers.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Правильные ответы:</span></p></body></html>"))
        self.mistakes.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Ошибки:</span></p></body></html>"))
        self.english_word.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">EngWord</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Выбери правильный перевод"))
        self.answer_button.setText(_translate("MainWindow", "Ответить"))
        self.skip_button.setText(_translate("MainWindow", "Пропустить"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600;\">Тестирование</span></p></body></html>"))
        self.translation3.setText(_translate("MainWindow", "translation3"))
        self.translation1.setText(_translate("MainWindow", "translation1"))
        self.translation2.setText(_translate("MainWindow", "translation2"))
        self.translation4.setText(_translate("MainWindow", "translation4"))
        self.back_from_testing_button.setText(_translate("MainWindow", "На главную"))
