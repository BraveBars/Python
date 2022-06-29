# 1. Площадь треугольника. Даны длины сторон треугольника. Вычислите площадь треугольника.
a, b, c = float(input()), float(input()), float(input())
p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c))**0.5
print('{0:.6f}'.format(S))

# 2. Сумма ряда. По данному числу n вычислите сумму (1 / 1²)+(1 / 2²)+(1 / 3²)+...+(1 / n²).
n = float(input())
c = 1
b = 0
while c <= n:
    a = (1 / c**2)
    b += a
    c += 1
print('{0:.5f}'.format(b))

# 3. Дробная часть. Дано положительное действительное число X. Выведите его дробную часть.
n = float(input())
print(n - int(n))
# более простое решение
print(float(input()) % 1)

# 4. Цена товара. Цена товара обозначена в рублях с точностью до копеек, то есть действительным
# числом с двумя цифрами после десятичной точки. Запишите в две целочисленные переменные
# стоимость товара в виде целого числа рублей и целого числа копеек и выведите их на экран.
# При решении этой задачи нельзя пользоваться условными инструкциями и циклами.
n = float(input())
print(int(n), round((n - int(n))*100))

# 5. Округление по российским правилам. По российский правилам числа округляются до ближайшего целого
# числа,а если дробная часть числа равна 0.5, то число округляется вверх. Дано неотрицательное число
# x, округлите его по этим правилам. Обратите внимание, что функция round не годится для этой задачи!
import math
n = float(input())
if n % 1 >= 0.5:
    print(math.ceil(n))
else:
    print(int(n))
# более простое решение
from math import floor
print(floor(float(input()) + 0.5))
# самое простое
print(int(float(input()) + 0.5))

# 6. Проценты. Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме
# вклада. Вклад составляет X рублей Y копеек. Определите размер вклада через год. При решении этой
# задачи нельзя пользоваться условными инструкциями и циклами.
p, x, y = int(input()), int(input()), int(input())
c = x * 100 + y
per = p * c / 100 + c
print(int(per // 100), int(per % 100))

# 7. Сложные проценты. Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются
# к сумме вклада через год. Вклад составляет X рублей Y копеек. Определите размер вклада через K лет.
# Программа должна вывести два числа: величину вклада через K лет в рублях и копейках. Дробное число
# копеек по истечение года отбрасывается. Перерасчет суммы вклада (с отбрасыванием дробных частей
# копеек) происходит ежегодно.
p, x, y, k = int(input()), int(input()), int(input()), int(input())
c = x * 100 + y
count = 1
per = p * c / 100 + c
while count < k:
    count += 1
    d = int(per) * p / 100 + int(per)
    per = d
print(int(per // 100), int(per % 100))

# 8. Квадратное уравнение - 1. Даны действительные коэффициенты a, b, c, при этом a != 0.
# Решите квадратное уравнение ax²+bx+c=0 и выведите все его корни.
a, b, c = float(input()), float(input()), float(input()),
d = b**2 - 4 * a * c
x = (-b + d**0.5) / (2 * a)
y = (-b - d**0.5) / (2 * a)
if d > 0 and x > y:
    print('{0:.6f}'.format(y), '{0:.6f}'.format(x))    # формат выше не нужен
if d > 0 and y > x:
    print('{0:.6f}'.format(x), '{0:.6f}'.format(y))
if d == 0:
    print('{0:.6f}'.format(x))
# похожее решение, но с квадратным корнем
import math
a, b, c = float(input()), float(input()), float(input()),
d = b**2 - 4 * a * c
if d > 0:
    x = (-b + math.sqrt(d)) / (2 * a)
    y = (-b - math.sqrt(d)) / (2 * a)
if d == 0:
    print((-b + math.sqrt(d)) / (2 * a))
elif d > 0 and x > y:
    print(y, x)
elif d > 0 and y > x:
    print(x, y)

# 9. Квадратное уравнение - 2. Даны произвольные действительные коэффициенты a, b, c. Решите уравнение
# ax²+bx+c=0. Если данное уравнение не имеет корней, выведите число 0. Если уравнение имеет один
# корень, выведите число 1, а затем этот корень. Если уравнение имеет два корня, выведите число 2,
# а затем два корня в порядке возрастания. Если уравнение имеет бесконечно много корней, выведите
# число 3.
import math
a, b, c = float(input()), float(input()), float(input()),
d = b**2 - 4 * a * c
if d < 0 or a == b == 0 and c != 0:
    print(0)
elif a == b == c == 0:
    print(3)
elif d > 0 and a != 0:
    x = (-b + math.sqrt(d)) / (2 * a)
    y = (-b - math.sqrt(d)) / (2 * a)
    if x > y:
        print(2, y, x)
    else:
        print(2, x, y)
elif d == 0 and a != 0:
    print(1, (-b + math.sqrt(d)) / (2 * a))
elif a == 0:
    print(1, -c / b)

# 10. Система линейных уравнений - 1. Даны вещественные числа a, b, c, d, e, f. Известно, что система
# линейных уравнений:
# ax + by = e
# cx + dy = f
# имеет ровно одно решение. Выведите два числа x и y, являющиеся решением этой системы.
a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
x = (d * e - f * b) / (d * a - b * c)
y = (f * a - e * c) / (d * a - b * c)
print(x, y)

# 11. Делаем срезы.
# Сначала выведите третий символ этой строки.
# Во второй строке выведите предпоследний символ этой строки.
# В третьей строке выведите первые пять символов этой строки.
# В четвертой строке выведите всю строку, кроме последних двух символов.
# В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0,
# поэтому символы выводятся начиная с первого).
# В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа
# строки.
# В седьмой строке выведите все символы в обратном порядке.
# В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
# В девятой строке выведите длину данной строки.
s = input()
print(s[2], s[-2], s[0:5], s[0:-2], s[::2],
      s[1::2], s[::-1], s[::-2], len(s), sep='\n')