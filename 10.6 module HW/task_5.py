# Задание 5. Наибольшая сумма цифр

count_num = int(input("Введите количество чисел: "))

def sum_digits(n):
    if n == 0:
        return n
    else:
        return int(n%10)+ sum_digits(int(n/10))
max_num = 0
max_sum = 0
for i in range(count_num):
    num = int(input("Введите число: "))
    if sum_digits(num) > max_sum:
        max_sum = sum_digits(num)
        max_num = num

print(f"Число {max_num} имеет максимальную сумму цифр: {max_sum}")