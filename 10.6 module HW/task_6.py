# Задание 6. Треугольник из хештегов

height = int(input("Ввелите высоту треугольника: "))
count = height - 1
count_hashtag = 1
for i in range(height):
    print(" " * count + "#" * count_hashtag)
    count -= 1
    count_hashtag +=2
