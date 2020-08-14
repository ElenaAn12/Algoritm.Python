# В программе генерируется случайное целое число
# от 0 до 100. Пользователь должен его отгадать не
# более чем за 10 попыток.После каждой неудачной попытки
# должно сообщаться, больше или меньше введенное пользователем
# число, чем то, что загадано.Если за 10 попыток число
# не отгадано, вывести правильный ответ.

import random


def guess(i, a, usnum):
    if usnum == a:
        print('Поздравляю! Вы угадали!')
        if input('Хотите попробовать еще раз? да/нет ').lower() in ['да', 'yes', 'д', 'y', 'lf']:
            i = 1
            guess(i, random.randint(0, 100), int(input('Угадай число от 0 100 за 3 попытки.\nПопытка №1: ')))
    elif i == 10:
        print(f'Попытки кончились. Вы проиграли, ответ: {a}')
        if input('Хотите попробовать еще раз? да/нет ').lower() in ['да', 'yes', 'д', 'y', 'lf']:
            i = 1
            guess(i, random.randint(0, 100), int(input('Угадай число от 0 100 за 3 попытки.\nПопытка №1: ')))
    else:
        if usnum < a:
            print(f'Введённое число меньше загаданного')
        else:
            print(f'Введённое число больше загаданного')
        i += 1
        guess(i, a, int(input('Попытка №' + str(i) + ': ')))


guess(1, random.randint(0, 100), int(input('Угадай число от 0 100 за 3 попытки.\nПопытка №1: ')))
