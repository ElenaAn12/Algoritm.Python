# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений. Завершение программы должно выполняться
# при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак
# (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль,
# если он ввел его в качестве делителя.

# https://drive.google.com/file/d/1yC2FdTaFQwfPIURJQrEWu9nEuct-gGJk/view?usp=sharing

def operation(a, b, oper):
    if oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    elif oper == '/':
        if b != 0:
            return a / b
        else:
            return a


def calculator(res, oper, counter):
    if oper != '0':
        if counter % 2 == 0:
            a = int(input('Введите число: '))
            if counter == 0:
                calculator(a, '', counter+1)
            else:
                r = operation(res, a, oper)
                if a == 0 and oper == "/":
                    print('На ноль делить нельзя. ')
                else:
                    print(f'{res} {oper} {a} = {r}')
                calculator(r, '', counter+1)
        else:
            oper = input('Ведите операцию: ')
            if oper in '+-*/0':
                calculator(res, oper, counter+1)
            else:
                print('Неправильная операция, повторите')
                calculator(res, '', counter)
    else:
        print('Результат: ', str(res))


calculator(0, '', 0)
