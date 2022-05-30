# Максимум из двух. Напишите программу, которая считывает
# два целых числа A и B и выводит наибольшее значение из них.
# Числа — целые от 1 до 1000.
a = int(input())
b = int(input())
if a > b:
    print(a)
else:
    print(b)

# Какое число больше? Даны два целых числа. Программа должна
# вывести число "1", если первое число больше второго,
# число "2", если второе больше первого или число "0", если они равны.
x = int(input())
y = int(input())
if x >= y:
    if x == y:
        print(0)
    else:
        print(1)
else:
    print(2)

# Високосный год. Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если год является
# високосным, то выведите YES, иначе выведите NO. Напомним, что в
# соответствии с григорианским календарем, год является високосным,
# если его номер кратен 4, но не кратен 100, или же если он кратен 400.
x = int(input())
if x % 4 == 0 and x % 100 > 0:
    print('Yes')
elif x % 400 == 0:
    print('Yes')
else:
    print('NO')

# Максимум трех чисел. Даны три целых числа. Найдите наибольшее из них
# (программа должна вывести ровно одно целое число).
x = int(input())
y = int(input())
z = int(input())
if y <= x >= z:
    print(x)
elif x <= y >= z:
    print(y)
else:
    print(z)

# Ход короля. Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.
# Даны две различные клетки шахматной доски, определите, может ли король попасть с первой клетки
# на вторую одним ходом.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if -1 <= a - c <= 1 and -1 <= b - d <= 1:
    print('yes')
else:
    print('No')

# Цвет клеток шахматной доски. Заданы две клетки шахматной доски. Если они покрашены в один цвет,
# то выведите слово YES, а если в разные цвета – то NO.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a + b) % 2 == 0 and (c + d) % 2 == 0:
    print('Yes')
elif (a + b + 1) % 2 == 0 and (c + d + 1) % 2 == 0:
    print('Yes')
else:
    print('No')

# Шоколадка. Шоколадка имеет вид прямоугольника, разделенного на n×m
# долек. Шоколадку можно один раз разломить по прямой на две части.
# Определите, можно ли таким образом отломить от шоколадки часть,
# состоящую ровно из k долек.
n = int(input())
m = int(input())
k = int(input())
if n * m > k and n * m * k > 0 and (k % m == 0 or k % n == 0):
    print('Yes')
else:
    print('No')