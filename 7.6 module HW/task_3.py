#Задача 3. Успеваемость в классе
count_satisfactory = 0
count_good = 0
count_perfect = 0
for count_student in range(int(input("Сколько в классе учеников? "))):
    temp = int(input("Введите оценку ученика: "))
    if temp == 3:
        count_satisfactory += 1
    elif temp == 4:
        count_good += 1
    else:
        count_perfect += 1

if count_satisfactory > count_good and count_satisfactory > count_perfect:
    print("Сегодня больше троешников!")
elif count_good > count_satisfactory and count_good > count_perfect:
    print("Сегодня больше хорошистов!")
else: print("Сегодня больше отличников! ")
