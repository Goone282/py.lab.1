import math

print("Выберите вариант (1–4):")
variant = int(input())

try:
    if variant == 1:
        a = float(input("Введите a: "))
        b = float(input("Введите b: "))
        c = float(input("Введите c: "))

        if a * b < -2:
            p = math.sqrt(abs(a * b)) + 2 * c
        elif -2 <= a * b <= 2:
            p = a**3 + b**2 - c**2
        else:  # a * b > 2
            p = a**c - b

        print("p =", p)

    elif variant == 2:
        x = float(input("Введите x: "))
        y = float(input("Введите y: "))

        if x < y:
            h = math.atan(x + abs(y))
        elif x > y:
            h = math.atan(abs(x + y))
        else:  # x == y
            h = (x + y) ** 2

        print("h =", h)

    elif variant == 3:
        x = float(input("Введите x: "))
        y = float(input("Введите y: "))

        if y > 0:
            b = math.log(abs(x / y)) + (x**2 + y)**3
        elif y < 0:
            b = math.log(abs(x / y)) + (x**2 + y**3)
        elif x == 0:
            b = x**2 + y**3
        else:  # y == 0
            b = 0

        print("b =", b)

    elif variant == 4:
        x = float(input("Введите x: "))
        y = float(input("Введите y: "))

        if x - y > 0:
            b = math.sin(x + y) + 2 * (x + y) ** 2
        elif x - y < 0:
            b = math.sin(x - y) + (x - y) ** 3
        elif x == 0:
            b = x**2 + math.sqrt(abs(y))
        else:  # y == 0
            b = 0

        print("b =", b)

    else:
        print("Неверный номер варианта")

except ValueError:
    print("Ошибка: введено нечисловое значение")
except ZeroDivisionError:
    print("Ошибка: деление на ноль")
