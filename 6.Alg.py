# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

list_ = random.sample(range(100), 10)

print(f'Список а:\n{list_}\n')
min_ = list_[0]
max_ = list_[0]
min_id = 0
max_id = 0

for i in range(len(list_) - 1):
    list_2 = []
    summa = 0
    if list_[i] <= min_:
        min_ = list_[i]
        min_id = i
    if list_[i] >= max_:
        max_ = list_[i]
        max_id = i

    # --------------- Первый способ

    if min_id < max_id:
        list_2.append(list_[min_id + 1:max_id])
        for j in list_2[0]:
            summa += j

    elif min_id > max_id:
        list_2.append(list_[max_id + 1:min_id])
        for j in list_2[0]:
            summa += j

list_[min_id] = max_
list_[max_id] = min_

# print(f'Максимальное число: {max_} \nзанимает позицию: {max_id}'
#       f'\nМинимальное число: {min_} \nзанимает позицию: {min_id}')
print(f'Сумма чисел {list_2[0]} = {summa}')


# ---------- Второй способ


# if min_id < max_id:
#     start_ = min_id
#     stop_ = max_id
# else:
#     start_ = max_id
#     stop_ = min_id
# sum_ = 0
# for j in range(abs(stop_ - start_ - 1)):
#     sum_ += list_[start_ + 1 + j]
# print('sum = ', sum_)
