eur = input("Введите сумму в долларах: ")
def doll (eur):
    try:
        return round(int(eur)/1.17,2)
    except ValueError:
        print("Недопустиое значение, вводите только числа")
print(doll(eur))
