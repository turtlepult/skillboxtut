begin_section = int(input("Введите начало отрезка: "))
end_section = int(input("Введите конец отрезка: "))
step = int(input("Введите шаг: "))
if step > 0:
    step = -step

if end_section < begin_section:
    end_section, begin_section = begin_section, end_section


def calculation(x):
    res = x ** 3
    temp = x ** 2 * 2
    res += temp
    temp = 4 * x
    res -= temp
    res += 1
    return res


for func_x in range(end_section, begin_section - 1, step):
    print(f"В точке {func_x} функция равна {calculation(func_x)}")
