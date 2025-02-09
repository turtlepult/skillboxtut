# Задача 1. «Я стал новым пиратом!»
count = 0
for scream in range(10):
    if input("Введите приветсвенный крик: ").lower() == "карамба":
        count += 1
    continue
print(f"Новых пиратов {count}")
