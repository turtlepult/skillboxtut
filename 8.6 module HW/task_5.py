# Задача 5. Стипендия

educational_grant = int(input("Введите ежемесячную стипендию: "))
expenses = int(input("Введите ежемесячные расходы: "))
extra_limit = 0
for mounth in range(1, 11):
    extra_limit += expenses - educational_grant
    print(f"{mounth}-й месяц: траты {expenses} рублей, не хватает {expenses - educational_grant} рублей.")
    percent = expenses / 100 * 3
    expenses += int(percent)

print(f"Сумма денег, которую необходимо получить у родителей: {extra_limit} рублей.")
