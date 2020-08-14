# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

def skin_walker(us_num, result):
    if us_num <= 0:
        print(f'Перевернутое число - {result}')
        return
    result = (result + us_num % 10 / 10) * 10
    skin_walker(int((us_num - us_num % 10) / 10), int(result))


skin_walker(int(input('Введите число: ')), 0)
