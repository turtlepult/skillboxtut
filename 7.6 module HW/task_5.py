#Задача 5. Замечательные числа
print(f"Замечательные числа в диапазоне Двузначных:")
for number in range(10,99):
    first_number = number//10
    second_number = number % 10
    if first_number * second_number * 3 == number:
        print(number)
