#Задание 3. Рамка

height = int(input("Введите высоту рамки: "))
width = int(input("Введите ширину рамки: "))

for i in range(height):
    print("|", end = "")
    for k in range(width):
        if i != 0 and i != height -1:
            print(" " * (width - 2), end="")
        else:
            print("-" * (width - 2), end="")
    print("|")