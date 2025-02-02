# Задача 4. Отрезок
temp = 0
count = 0
start_position = int(input("Начало отрезка: "))
end_position = int(input("Конец отрезка: "))
print("Числа из отрезка, которые делятся на 3:")
for section in range(start_position, end_position + 1):
    if section % 3 == 0:
        count += 1
        print(section)
        temp += section
print(f"Среднее арифметическое этих чисел: {temp / count}")
