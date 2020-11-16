from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import testing
import words_input
import pickle
import random



class mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.begin_testing_button.clicked.connect(self.start_testing_button_clicked)
        self.ui.upload_word_button.clicked.connect(self.upload_word_button_clicked)
        self.testing_window = testing_window()
        self.words_input_window = words_input_window()

    def upload_word_button_clicked(self):
        self.words_input_window.show()

    def start_testing_button_clicked(self):
        self.testing_window.show()


class testing_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(testing_window, self).__init__()
        self.ui = testing.Ui_MainWindow()
        self.ui.setupUi(self)
        self.get_values()
        self.button_group = QtWidgets.QButtonGroup()
        self.button_group.addButton(self.ui.translation1)
        self.button_group.addButton(self.ui.translation2)
        self.button_group.addButton(self.ui.translation3)
        self.button_group.addButton(self.ui.translation4)
        self.correct_answers = 0
        self.mistakes = 0
        self.ui.answer_button.clicked.connect(self.answer_button_clicked)
        self.ui.skip_button.clicked.connect(self.skip_button_clicked)
        self.ui.back_from_testing_button.clicked.connect(self.back_from_testing_button_clicked)


    def get_values(self):
        with open('eng_rus_dict.pickle', 'rb') as f:
            data = pickle.load(f)
        words = set()
        for i in range(4):
            word = random.choice(list(data.keys()))
            while word in words:
                word = random.choice(list(data.keys()))
            words.add(word)
        word_list = [data[i] for i in words]
        random.shuffle(word_list)
        my_word = words.pop()
        self.ans = data.get(my_word)
        self.ui.english_word.setText(my_word)
        self.ui.translation1.setText(word_list[0])
        self.ui.translation2.setText(word_list[1])
        self.ui.translation3.setText(word_list[2])
        self.ui.translation4.setText(word_list[3])

    def answer_button_clicked(self):
        otwet = self.button_group.checkedButton()
        if otwet.text() == self.ans:
            self.correct_answers += 1
        else:
            self.mistakes += 1
        self.ui.correct_answers_label.setText(str(self.correct_answers))
        self.ui.wrong_answers_label.setText(str(self.mistakes))
        self.get_values()

    def skip_button_clicked(self):
        self.mistakes += 1
        self.ui.wrong_answers_label.setText(str(self.mistakes))
        self.get_values()

    def back_from_testing_button_clicked(self):
        self.close()



class words_input_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(words_input_window, self).__init__()
        self.ui = words_input.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ok_button.clicked.connect(self.ok_button_clicked)
        self.ui.back_button.clicked.connect(self.back_button_clicked)

    def ok_button_clicked(self):
        translation_input = self.ui.translation_input.text()
        word_input = self.ui.word_input.text()
        if translation_input == '' or word_input == '':
            pass
        else:
            with open('eng_rus_dict.pickle', 'rb') as f:
                data = pickle.load(f)
            data[word_input] = translation_input
            with open('eng_rus_dict.pickle', 'wb') as f:
                pickle.dump(data, f)
            self.ui.translation_input.clear()
            self.ui.word_input.clear()

    def back_button_clicked(self):
        self.close()


app = QtWidgets.QApplication([])
application = mainwindow()
application.show()

sys.exit(app.exec())



