word = input("enter something here... ")
print(len(word))
if len(word)>10:
    print(word[:10])


import random
import time


eng_words = ['Hi','Bye','Task', 'Programm']
ru_words = ['Привет','Пока','Задача', 'Программа']
score = 0

mod = input("Выбери режим работы тренажера: 0 - добавить новые слова, 1 - тренироваться: \n")
while ((mod != '0') and (mod != '1')):
    mod = input("Недопустимый символ! Выбери 0 или 1. (0 - добавить новые слова, 1 - тренироваться) \n")

if mod == "1":
    print("Переведи как можно больше слов правильно! У тебя 10 попыток!")
    for i in range(10):
        number = random.randint(0, len(eng_words))
        print("Как переводится слово: " + eng_words[number])
        if input() == ru_words[number]:
            print("Отлично!!!")
            score += 1
        else:
            print("Нет... Это слово - " + ru_words[number])
else:
    word = input("Введите слово на русском языке: ")
    translate = input("Введите перевод этого слова: ")
    if len(word) > 0 and len(translate) > 0:
        ru_words.append(word)
        eng_words.append(translate)
        print("Слово успешно добавлено!")




game = input("Let`s play a game! You`re in?")
ger_words = ['Hallo','Tschüss','Aufgabe', 'Programm']
ru_words = ['Привет','Пока','Задача', 'Программа']
score = 0
number = int(input("Choose 0 or 1"))
while number !=0 and number !=1:
    print("Choose only 0 or 1")
if number == 0 :
    print("You need to translate the word correctly! You have 10 attempts!")
    for i in range(10):
        i = random.randint(ger_words[i])
        print("What is the translation of the word: " + ger_words[i])
        if input() == ru_words[i]:
            print("Good job!!!")
            score +=1
elif number == 1:
    word = input("Enter a word in German:")
    translation = input("Enter a translation of this word:")
    print("Word successfully added!")
    ger_words.append(word)
    ru_words.append(translation)
    print(ger_words[i], "-", ru_words[i])
