# Задание 2. Лестница

ladder = int(input("Введите число: "))
count = 1
for i in range(ladder):
    print((str(count) + " ") * count)
    count += 1