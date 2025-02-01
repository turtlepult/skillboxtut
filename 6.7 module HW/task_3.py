from random import randint

'''
Максим программирует целый день на работе и вечером идёт домой. Каждый час начальство кидает ему несколько задач,
которые нужно решить до следующего рабочего часа. Вдобавок каждый час Максиму звонит супруга.
Он знает, что если возьмёт трубку, то жена попросит зайти вечером в магазин.
Что нужно сделать
Напишите программу, в которой считается, сколько задач выполнил Максим за день (восемь часов).
Если он хотя бы раз взял трубку, то в конце дополнительно выводите сообщение: «Нужно зайти в магазин».
Дополнительно: сделайте так, чтобы жена не звонила Максиму, если он уже хотя бы раз ответил на звонок в течение рабочего дня.
'''
print("Начался восьмичасовой рабочий день.")
count_hours = 1
tasks = 0
flag = True
while count_hours <= 8:
    print(f"{count_hours}-й час")
    random = randint(1, 5)
    print(f"Сколько задач решит Максим? {random}")
    tasks += random
    if flag:
        random_calling_wife = randint(0, 1)
        print(f"Звонит жена. Взять трубку? (1 — да, 0 — нет): {random_calling_wife}")
        if random_calling_wife == 1:
            flag = False
    else:
        pass
    count_hours += 1
print(f"Рабочий день закончился. Всего выполнено задач: {tasks}")
if flag != True:
    print("Нужно зайти в магазин.")
