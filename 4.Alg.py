# Определить, какое число в массиве встречается чаще всего.

from random import randint
import random


def t(list_len=10):
    list_ = []
    max_count = 0
    max_digit = 0
    while len(list_) < list_len:
        r = randint(0, 5)
        list_.append(r)
    print(list_)
    for i in range(len(list_)):
        num = list_.count(list_[i])
        if max_count < num:
            max_count = num
            max_digit = list_[i]
    print(f'Число {max_digit}, содержиться в массиве {max_count} раз(а)')


t()

# ---------- 2 Вариант


# def t(list_len=9):
#     list_ = []
#     max_count = 0
#     max_digit = 0
#     while len(list_) < list_len:
#         r = randint(0, 5)
#         list_.append(r)
#     print(list_)
#     for i in range(len(list_)):
#         count_ = 0
#         for j in range(len(list_)):
#             if list_[j] == list_[i]:
#                 count_ += 1
#         if max_count <= count_:
#             max_count = count_
#             max_digit = list_[i]
#     print(f'Число {max_digit}, содержиться в массиве {max_count} раз(а)')
#
#
# t()

# -------------3 Вариант


# def t(list_len):
#     list_ = []
#     while len(list_) < list_len:
#         r = random.randint(0, 5)
#         list_.append(r)
#     return list_
#
#
# def find_max_count(l):
#     print(l)
#     max_digit = 0
#     max_count = 0
#     for i in range(len(l)):
#         save_ = l[i]
#         count_ = 0
#         for j in range(len(l)):
#             if l[j] == save_:
#                 count_ += 1
#         if max_count < count_:
#             max_count = count_
#             max_digit = save_
#     print(f'Число {max_digit}, встречается {max_count} раз(а)')
#
#
# find_max_count(t(10))
