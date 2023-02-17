rub = input("Введите сумму в долларах: ")
def doll (rub):
    try:
        return round(int(rub)/1.17,2)
    except ValueError:
        print("Недопустиое значение, вводите только числа")
print(doll(rub))
