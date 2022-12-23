""" Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов."""

a = int(input("Введите число "))
b = int(input("Введите число "))
c = int(input("Введите число "))
d = [a,b,c]
def my_func(*d):
    print(sum(sorted(list(d), reverse=False)[1:]))
print(my_func(*d))