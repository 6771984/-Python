""" Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов."""

a = int(input("Введите число "))
b = int(input("Введите число "))
c = int(input("Введите число "))
d = [a,b,c]
def get_max(*d):
    print(sum(sorted(list(d), reverse=False)[1:]))
print(get_max(*d))