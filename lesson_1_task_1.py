""" Поработайте с переменными, создайте несколько, выведите на экран.
Запросите у пользователя некоторые числа и строки и сохраните в переменные,
затем выведите на экран."""

text = input ("Введите слово: ")
letter_number = int(input ("Выберите номер буквы: "))-1
letter = text[letter_number]
print (f"Буква: {letter}")