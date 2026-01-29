import math

print("Выберите вариант (1–4):")
variant = int(input())

try:
    if variant == 1:
        x = float(input("Введите x: "))
        y = float(input("Введите y: "))
        z = float(input("Введите z: "))

        denominator = z + x**2 / 4
        if denominator == 0:
            print("Ошибка: деление на ноль")
        else:
            k = math.log(abs(y - math.sqrt(abs(x)))) * (x - y / denominator)
            print("k =", k)

    elif variant == 2:
        x = float(input("Введите x: "))
        y = float(input("Введите y: "))

        denominator = 0.5 + math.sin(y)**2
        if denominator == 0:
            print("Ошибка: деление на ноль")
        else:
            d = (2 * math.cos(x - math.pi / 6)) / denominator + abs(y - x) / 3
            print("d =", d)

    elif variant == 3:
        x = float(input("Введите x: "))
        y = float(input("Введите y: "))
        z = float(input("Введите z: "))

        denominator = math.sin(y)**2 - (math.sin(x) * math.sin(y))**2
        if denominator == 0:
            print("Ошибка: деление на ноль")
        else:
            w = ((x / y) * (z + x) * math.exp(abs(x - y)) + math.log(1 + math.e)) / denominator
            print("w =", w)

    elif variant == 4:
        x = float(input("Введите x: "))
        y = float(input("Введите y: "))
        z = float(input("Введите z: "))

        denominator = 1 + x**2 * abs(y - math.tan(z))
        if denominator == 0:
            print("Ошибка: деление на ноль")
        else:
            b = (3 + math.exp(y - 1)) / denominator
            print("b =", b)

    else:
        print("Неверный номер варианта")

except ValueError:
    print("Ошибка: введено нечисловое значение")
