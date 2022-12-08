"""Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операци"""
number = input("Ведите целое положительное число: ")
number_length = len(number)
index = 0
max_num = 0
while index != number_length:
    # достаем очередную цифру числа с начала
    cur_n = int(number [index])
    if max_num < cur_n:
        max_num = cur_n
    index +=1

print(f"Самая большая цифра в числе: {max_num}")