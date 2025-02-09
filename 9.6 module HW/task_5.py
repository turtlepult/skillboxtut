#Задача 5. Коровы

stall = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

total_milk = 0

input_value = input("Введите 10 стойл в одну строку. a — свободное стойло, b — занятое: ")

for count, letter in enumerate(input_value):
    if letter == "b":
        total_milk += stall[count]

print(f"Произведено молока за день: {total_milk}")