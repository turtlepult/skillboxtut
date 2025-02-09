# Задача 2. Театр

row = int(input("Введите количество рядов: "))
numberOfSeats = int(input("Введите количество сидений в ряде: "))
countMeters = int(input("Введите количество метров между рядами: "))

print("\n Сцена \n")

for i in range(row):
    print("=" * numberOfSeats, "*" * countMeters, "=" * numberOfSeats, )
