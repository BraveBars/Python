# 1. Максимум из двух. Напишите программу, которая считывает
# два целых числа A и B и выводит наибольшее значение из них.
# Числа — целые от 1 до 1000.
a = int(input())
b = int(input())
if a > b:
    print(a)
else:
    print(b)

# 2. Какое число больше? Даны два целых числа. Программа должна
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

# 3. Високосный год. Дано натуральное число. Требуется определить,
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

# 4. Максимум трех чисел. Даны три целых числа. Найдите наибольшее из них
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

# 5. Ход короля. Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.
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

# 6. Цвет клеток шахматной доски. Заданы две клетки шахматной доски. Если они покрашены в один цвет,
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

# 7. Шоколадка. Шоколадка имеет вид прямоугольника, разделенного на n×m
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

# 8. На шахматной доске стоит белая шашка. Требуется определить, может ли она попасть в заданную
# клетку, делая ходы по правилам и не пользуясь ходами дамки (т. е. не используя возможность
# перемещаться назад после превращения в дамку). Белые шашки могут ходить по клеткам одного
# цвета по диагонали вверх-влево или вверх-вправо. Ходов может быть несколько!
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a + b + c + d) % 2 == 0 and a + b <= c + d and b < d:
    print('Yes')
else:
    print('No')

# 9. Даны три целых числа A, B, C. Определить, есть ли среди них хотя бы
# одно четное и хотя бы одно нечетное.
a = int(input())
b = int(input())
c = int(input())
if (a % 2 == 0 or b % 2 == 0 or c % 2 == 0) and \
        ((a + 1) % 2 == 0 or (b + 1) % 2 == 0 or (c + 1) % 2 == 0):
    print('Yes')
else:
    print('No')
# Более красивое решение
a, b, c = int(input()), int(input()), int(input())
if 0 < a % 2 + b % 2 + c % 2 < 3:
    print('YES')
else:
    print('NO')

# 10. Сколько совпадает чисел. Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает)
# или 0 (если все числа различны).
n = int(input())
m = int(input())
k = int(input())
if n == m and n == k and k == m:
    print(3)
elif n == m or n == k or k == m:
    print(2)
else:
    print(0)

# 11. Коровы. Программа должна вывести введенное число n и одно из слов: korov, korova или korovy,
# правильно склоняя слово “korova”. Между числом и словом должен стоять ровно один пробел.
n = int(input())
if 10 < n < 20 or 5 <= n % 10 <= 9 or n % 10 == 0:
    print(n, 'korov')
elif n % 10 == 1:
    print(n, 'korova')
else:
    print(n, 'korovy')

# В математике функция sign(x) (знак числа) определена так:
# sign(x)=1, если x>0,
# sign(x)=-1, если x<0,
# sign(x)=0, если x=0.
# Для данного числа x выведите значение sign(x).
x = int(input())
if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)