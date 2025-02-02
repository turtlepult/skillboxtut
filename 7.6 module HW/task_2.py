# Задача 2. Посчитай чужую зарплату...
total_average_salary = 0
for average_salary in range(12):
    mounth_salary = int(input("Введите зарплату сотрудника: "))
    total_average_salary += mounth_salary
print(f"Количество корректных номеров (чётных и положительных): {total_average_salary / 12}")
