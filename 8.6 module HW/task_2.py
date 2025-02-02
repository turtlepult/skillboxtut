# Задача 2. Долги
from random import randint

total_debt = 0
count = 0
for debtor in range(int(input("Введите количество должников: "))):
    if count % 5 == 0:
        debt = randint(1000, 5000)
        total_debt += debt
        print(f"Должник с номером {count}\n Сколько должны? {debt}")
    count += 1
print(f"Общая сумма долга: {total_debt}")
