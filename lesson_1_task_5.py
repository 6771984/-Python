"""Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма.
Например, прибыль — выручка больше издержек,
или убыток — издержки больше выручки.
Выведите соответствующее сообщение."""

revenue = int(input("Укажите текущую выручку Вашей фирмы: "))
cost = int(input("Укажите текущие расходы Вашей фирмы: "))
profit = revenue - cost
if profit > 0:
    print(f"Прибыль Вашей компании: {profit}")
elif profit < 0:
    print(f"Убыток Вашей компании: {profit}")
else:
    print(f"Вы сработали в ноль")