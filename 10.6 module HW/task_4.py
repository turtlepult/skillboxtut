# Задание 4. Простые числа
count = 0

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


for i in range(int(input("Введите количество чисел: "))):
    num = int(input("Введите число: "))
    if is_prime(num):
        count += 1

print(f"Количество простых чисел в последовательности: {count}")