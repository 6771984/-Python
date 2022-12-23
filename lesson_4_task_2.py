"""Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для его формирования используйте генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123]."""

primary_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# вариант 1
new_lst_1 = []
for i in range(1, len(primary_list)):
    if primary_list[i] > primary_list[i - 1]:
        new_lst_1.append(primary_list[i])

print(new_lst_1)

# вариант 2
new_lst_2 = [primary_list[i] for i in range(1, len(primary_list))
     if primary_list[i] > primary_list[i - 1]]

print(new_lst_2)