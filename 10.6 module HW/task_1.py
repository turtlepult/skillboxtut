# Задание 1. Тестовое задание

for i in range(6):
    print(i, end="\t")
    temp = i + 2
    for k in range(5):
        print(temp, end="\t")
        temp += 2
    print()
