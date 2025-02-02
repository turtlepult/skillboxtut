# Задача 1. Космическая еда
print("Информация о запасах гречки:")
count = 0
for food_supply in range(100, -1, -4):
    if food_supply > 0:
        print(f"Через {count} месяц: {food_supply} кг гречки в запасе")
    elif food_supply == 0:
        print(f"Через {count} месяц: {food_supply} кг гречки в запасе")
        print("Запасы гречки закончились.")
    count += 1
