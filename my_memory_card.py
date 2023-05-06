from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QPushButton, QLabel, QGroupBox, QVBoxLayout, QHBoxLayout, QButtonGroup
from random import shuffle
from random import randint

class Questions():
    def __init__(self, question, right_answer, wrong_1, wrong_2, wrong_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(600, 400)
text = QLabel('Какой национальности не существует?')
button = QPushButton('Ответить')
RadioGroupeBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Алеуты')
vline1 = QVBoxLayout()
vline2 = QVBoxLayout()
vline1.addWidget(rbtn_1)
vline1.addWidget(rbtn_2)
vline2.addWidget(rbtn_3)
vline2.addWidget(rbtn_4)
hline = QHBoxLayout()
hline.addLayout(vline1)
hline.addLayout(vline2)
RadioGroupeBox.setLayout(hline)
RadioGroupe = QButtonGroup()
RadioGroupe.addButton(rbtn_1)
RadioGroupe.addButton(rbtn_2)
RadioGroupe.addButton(rbtn_3)
RadioGroupe.addButton(rbtn_4)
AnsGroupeBox = QGroupBox()
correct = QLabel('Правильно или неправильно')
r_answer = QLabel('Смурфы')
vline3 = QVBoxLayout()
vline3.addWidget(correct)
vline3.addWidget(r_answer)
AnsGroupeBox.setLayout(vline3)
AnsGroupeBox.hide()
v = QVBoxLayout()
v.addWidget(text)
v.addWidget(RadioGroupeBox)
v.addWidget(AnsGroupeBox)
v.addWidget(button)
main_win.setLayout(v)

def show_result():
    RadioGroupeBox.hide()
    AnsGroupeBox.show()
    button.setText('Следующий вопрос')
def show_question():
    RadioGroupeBox.show()
    AnsGroupeBox.hide()
    button.setText('Ответить')
    RadioGroupe.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroupe.setExclusive(True)
def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()


def next_question():  
    main_win.total +=1
    cur_question = randint(0,len(question_list)-1)
    ask(question_list[cur_question])
    print('Статистика')
    print('Всего вопросов', main_win.total)
    print('Правильных ответов', main_win.score)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Questions):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_1)
    answers[2].setText(q.wrong_2)
    answers[3].setText(q.wrong_3)
    text.setText(q.question)
    r_answer.setText(q.right_answer)
    show_question()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1 
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked:
            show_correct('Неправильно')
    print('Статистика')
    print('Всего вопросов', main_win.total)
    print('Правильных ответов', main_win.score)
    print('Рейтинг', main_win.score/main_win.total*100, '%')
            
def show_correct(res):
    correct.setText(res)
    show_result()
main_win.cur_question = -1
question_list = []
q = Questions('Государственный язык Бразилии', "Португальский", "Итальянский", 'Испанский', 'Французский')   
question_list.append(q)
question_list.append(Questions('Сколько на земле материков', '6', '10', '5', '7'))
question_list.append(Questions('Сколько лап у кошек', '4', '3', '6', '5'))
question_list.append(Questions('А я просто не знаю что писать', 'пон да', 'pon', 'тампон','k.nj'))
question_list.append(Questions('Что содержится в клетке', 'негры', 'чурки', 'микробы', 'я сама хз'))
question_list.append(Questions('У меня просто плохо с фантазией', 'боже', 'dct dct gjyzkb', 'и что', 'давай типа все норм'))
question_list.append(Questions('что делают кофейные зерна перед смертью?', 'молятся', 'взрываются', 'еще что то', 'ничего'))
question_list.append(Questions('что общего между негром и велосипедом?', 'оба работают только на цепи', 'ничего', 'хз', 'почему'))
question_list.append(Questions('в исламских государствах можно расплатится Visa, Mastercard, но там не принимают ', 'Mir', 'C,th,fyr ', 'Сбербанк', 'тинькофф'))
question_list.append(Questions('привет как дела?', 'пр отлично', 'привет', 'прпрпр', 'приветики'))
main_win.score = 0
main_win.total = 0
next_question()
button.clicked.connect(click_OK)

main_win.show()
app.exec_()

