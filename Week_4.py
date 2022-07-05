# 1. Минимум 4 чисел. Напишите функцию min4(a, b, c, d), вычисляющую минимум четырех чисел,
# которая не содержит инструкции if, а использует стандартную функцию min от двух чисел.
# Считайте четыре целых числа и выведите их минимум.
def min4(a, b, c, d):
    e = min(a, b)
    e2 = min(e, c)
    e3 = min(e2, d)
    return e3

a, b, c, d = input(), input(), input(), input()
print(min4(a, b, c, d))


# 2. Длина отрезка. Даны четыре действительных числа: x₁, y₁, x₂, y₂. Напишите функцию
# distance(x1, y1, x2, y2), вычисляющую расстояние между точками (x₁,y₁) и (x₂,y₂).
# Считайте четыре действительных числа и выведите результат работы этой функции.
def distance(x1, y1, x2, y2):
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2)**0.5
    return d

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
print(distance(x1, y1, x2, y2))


# 3. Периметр треугольника. Напишите функцию, вычисляющую длину отрезка по координатам его концов.
# С помощью этой функции напишите программу, вычисляющую периметр треугольника по координатам
# трех его вершин.
def perimeter(x1, y1, x2, y2, x3, y3):
    d = ((x2 - x1)**2 + (y2 - y1) ** 2)**0.5
    e = ((x3 - x2)**2 + (y3 - y2) ** 2)**0.5
    f = ((x3 - x1)**2 + (y3 - y1) ** 2)**0.5
    g = d + e + f
    return g

x1, y1, x2, y2, x3, y3 = int(input()), int(input()), int(input()),\
                         int(input()), int(input()), int(input())
print(perimeter(x1, y1, x2, y2, x3, y3))


# 4. Принадлежит ли точка квадрату - 1. Даны два действительных числа x и y(оба от -1 до 1).
# Проверьте, принадлежит ли точка с координатами (x,y) заштрихованному квадрату (включая его границу).
# Если точка принадлежит квадрату, выведите слово YES, иначе выведите слово NO.
# На рисунке сетка проведена с шагом 1.
#
# Решение должно содержать функцию IsPointInSquare(x, y), возвращающую True, если точка принадлежит
# квадрату и False, если не принадлежит. Основная программа должна считать координаты точки, вызвать
# функцию IsPointInSquare и в зависимости от возвращенного значения вывести на экран необходимое
# сообщение. Функция IsPointInSquare не должна содержать инструкцию if.
def IsPointInSquare(x, y):
    return abs(x) <= 1 and abs(y) <= 1

x, y = float(input()), float(input())
if IsPointInSquare(x, y):
    print('Yes')
else:
    print('No')
# БОЛЕЕ ИНТЕРЕНСЫЙ ВАРИАНТ РЕШЕНИЯ ЗАДАЧИ
def IsPointInSquare(x, y):
    return x**2 <= 1 and y**2 <= 1

a, b = float(input()), float(input())
print(IsPointInSquare(a, b) * 'YES' + 0**IsPointInSquare(a, b) * 'NO')


# 5. Принадлежит ли точка квадрату - 2. Даны два действительных числа x и y. Проверьте, принадлежит
# ли точка с координатами(x,y) заштрихованному квадрату (включая его границу). Если точка принадлежит
# квадрату, выведите слово YES,иначе выведите слово NO. На рисунке сетка проведена с шагом 1.
def IsPointInSquare(x, y):
    return abs(x) + abs(y) <= 1

x, y = float(input()), float(input())
if IsPointInSquare(x, y):
    print('Yes')
else:
    print('No')