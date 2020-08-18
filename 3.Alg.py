# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

import random

a = random.sample(range(100), 10)
print(f'Список а:\n{a}\n')
min_ = a[0]
max_ = a[0]
min_id = 0
max_id = 0

for i in range(len(a)-1):
    if a[i] <= min_:
        min_ = a[i]
        min_id = i
    if a[i] >= max_:
        max_ = a[i]
        max_id = i
a[min_id] = max_
a[max_id] = min_

print(f'Список измененный а:\n{a}\n')
print(f'Максимальное число:{max_},\nМинимальное число: {min_}')

# -------------- 2 Вариант

# import random
#
# a = random.sample(range(100), 10)
#
# max_ = 0
# min_ = 999999
# for i in a:
#     if i > max_:
#         max_ = i
#     if min_ > i:
#         min_ = i
#
# a[a.index(max_)], a[a.index(min_)] = a[a.index(min_)], a[a.index(max_)]
#
# print(a)
