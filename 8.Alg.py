# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в
# последнюю ячейку строки.
# В конце следует вывести полученную матрицу.


from random import random

M = 4
N = 4
a = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(int(random() * 11))
        print(b[j], " ",  end='')
    a.append(b)
    print('   |', f'{b[0] + b[1] + b[2] + b[3]}')
