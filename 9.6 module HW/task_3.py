# Задача 3. Марсоход-2
x_max = 15
y_max = 20

x = 8
y = 10


def going_beyond(x, y):
    if x > 15 or y > 20 or x < 0 or y < 0:
        return False
    else:
        return True


operation = input("Введите команду для движения или Q для выхода: ")

while operation != "Q":
    if operation == "W":
        x += 1
        if going_beyond(x, y):
            print("Марсоход находится на позиции", x, y, "введите команду: ")
            operation = input()
            continue
        else:
            x -= 1
            print("Марсоход находится на позиции", x, y, "введите команду: ")
            operation = input()

    elif operation == "S":
        x -= 1
        if going_beyond(x, y):
            print("Марсоход находится на позиции", x, y, "введите команду: ")
            operation = input()
            continue
        else:
            x += 1
            print("Марсоход находится на позиции", x, y, "введите команду: ")
            operation = input()

    elif operation == "A":
        y -= 1
        if going_beyond(x, y):
            print("Марсоход находится на позиции", x, y, "введите команду: ")
            operation = input()
            continue
        else:
            y += 1
            print("Марсоход находится на позиции", x, y, "введите команду: ")
            operation = input()

    elif operation == "D":
        y += 1
        if going_beyond(x, y):
            print("Марсоход находится на позиции", x, y, "введите команду: ")
            operation = input()
            continue
        else:
            y -= 1
            print("Марсоход находится на позиции", x, y, "введите команду: ")
            operation = input()

    elif operation == "Q":
        break
