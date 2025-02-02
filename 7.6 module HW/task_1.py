# Задача 1. Космический корабль
count = 0
for correct_number in range(10):
    check_number = int(input("Введите число: "))
    if check_number % 2 == 0:
        if check_number > 0:
            count += 1
        else:
            continue
    else:
        continue
print(f"Количество корректных номеров (чётных и положительных): {count}")
