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

# 12. В математике функция sign(x) (знак числа) определена так:
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

# 13. Мороженое. В кафе мороженое продают по три шарика и по пять шариков.
# Можно ли купить ровно k шариков мороженого?
n = int(input())
if n >= 3 and n != 4 and n != 7:
    print('Yes')
else:
    print('No')

# 14. Координатные четверти. Даны координаты двух точек на плоскости, требуется определить,
# лежат ли они в одной координатной четверти или нет (все координаты отличны от нуля).
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 * x2 > 0 and y1 * y2 > 0:
    print('Yes')
else:
    print('No')

# 15. Упорядочить три числа. Дано три числа. Упорядочите их в порядке
# неубывания. Программа должна считывать три числа a,b,c, затем
# программа должна менять их значения так, чтобы стали выполнены
# условия a≤b≤c, затем программа выводит тройку a,b,c.
a, b, c = int(input()), int(input()), int(input())
if a <= c <= b:
    (b, c) = (c, b)
elif b <= a <= c:
    (a, b) = (b, a)
elif b <= c <= a:
    (a, b, c) = (b, c, a)
elif c <= a <= b:
    (a, b, c) = (c, a, b)
elif c <= b <= a:
    (a, c) = (c, a)
print(a, b, c)

# 16. Коробки. Есть две коробки, первая размером A₁×B₁×C₁, вторая размером A₂×B₂×C₂.
# Определите, можно ли разместить одну из этих коробок внутри другой, при условии,
# что поворачивать коробки можно только на 90 градусов вокруг ребер.
# Программа должна вывести одну из следующих строчек:
# Boxes are equal, если коробки одинаковые,
# The first box is smaller than the second one, если первая коробка может быть положена во вторую,
# The first box is larger than the second one, если вторая коробка может быть положена в первую,
# Boxes are incomparable, во всех остальных случаях.
a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
if b1 > c1:
    (b1, c1) = (c1, b1)
if a1 > c1:
    (a1, c1) = (c1, a1)
if a1 > b1:
    (a1, b1) = (b1, a1)
if b2 > c2:
    (b2, c2) = (c2, b2)
if a2 > c2:
    (a2, c2) = (c2, a2)
if a2 > b2:
    (a2, b2) = (b2, a2)
if a1 == a2 and b1 == b2 and c1 == c2:
    print('Boxes are equal')
elif a1 <= a2 and b1 <= b2 and c1 <= c2:
    print('The first box is smaller than the second one')
elif a1 >= a2 and b1 >= b2 and c1 >= c2:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')

# Складирование ноутбуков. На склад, который имеет форму прямоугольного параллелепипеда,
# привезли ноутбуки, упакованные в коробки. Каждая коробка также имеет форму прямоугольного
# параллелепипеда. По правилам хранения коробки с ноутбуками должны быть размещены на складе
# с выполнением следующих двух условий:
#
#       Стороны коробок должны быть параллельны сторонам склада.
#
#       Коробку при помещении на склад разрешается расположить где угодно (с выполнением предыдущего
#       условия), в том числе на другой коробке, но все коробки должны быть
#       ориентированы одинаково (т.е. нельзя одну коробку расположить “стоя”, а другую —“лежа”)
#
# 17. Напишите программу, которая по размерам склада и размерам коробки с ноутбуком определит
# максимальное количество ноутбуков, которое может быть размещено на складе.
l1, h1, w1 = int(input()), int(input()), int(input())
l2, h2, w2 = int(input()), int(input()), int(input())
v1 = (l1 // l2) * (h1 // h2) * (w1 // w2)
v2 = (l1 // l2) * (h1 // w2) * (w1 // h2)
v3 = (l1 // h2) * (h1 // l2) * (w1 // w2)
v4 = (l1 // h2) * (h1 // w2) * (w1 // l2)
v5 = (l1 // w2) * (h1 // l2) * (w1 // h2)
v6 = (l1 // w2) * (h1 // h2) * (w1 // l2)
if v1 > v2:
    v2 = v1
if v2 > v3:
    v3 = v2
if v3 > v4:
    v4 = v3
if v4 > v5:
    v5 = v4
if v5 > v6:
    v6 = v5
print(v6)

# 18. Узник замка Иф. За многие годы заточения узник замка Иф проделал
# в стене прямоугольное отверстие размером D×E. Замок Иф сложен из
# кирпичей, размером A×B×C. Определите, сможет ли узник выбрасывать
# кирпичи в море через это отверстие (очевидно, стороны кирпича
# должны быть параллельны сторонам отверстия).
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
if (A <= D and B <= E) or (A <= E and B <= D):
    print('Yes')
elif (B <= D and C <= E) or (B <= E and C <= D):
    print('Yes')
elif (A <= D and C <= E) or (A <= E and C <= D):
    print('Yes')
else:
    print('No')

# 19. Список квадратов. По данному целому числу N распечатайте все
# квадраты натуральных чисел,не превосходящие N, в порядке возрастания.
n = int(input())
i = 1
while i <= n:
    if i**2 <= n:
        print(i**2, end=' ')
        i = i + 1
    else:
        break

# 20. Минимальный делитель. Дано целое число, не меньшее 2.
# Выведите его наименьший натуральный делитель, отличный от 1.
n = int(input())
i = 2
while i <= n:
    x = n % i
    if x == 0:
        print(i)
        break
    else:
        i = i + 1
# или более простой вариант
n = int(input())
i = 2
while n % i != 0:
    i = i + 1
print(i)

# 21. Список степеней двойки. По данному числу N распечатайте все целые
# степени двойки, не превосходящие N, в порядке возрастания.
# Операцией возведения в степень пользоваться нельзя!
n = int(input())
i = 2
if n >= 1:
    print(1, end=" ")
if n >= 2:
    print(2, end=" ")
while i <= n:
    i = i * 2
    if i <= n:
        print(i, end=' ')
    else:
        break
# более простое решение
n = int(input())
i = 1
while i <= n:
    print(i, end=' ')
<<<<<<< HEAD
    i = i * 2
=======
    i = i * 2

# 22. Точная степень двойки. Дано натуральное число N. Выведите слово
# YES, если число N является точной степенью двойки, или слово NO
# в противном случае. Операцией возведения в степень пользоваться нельзя!
n = int(input())
i = 1
while i <= n:
    if n == i:
        print('Yes')
        break
    else:
        i = i * 2
        if i > n:
            print('No')
# Двоичный логарифм. По данному натуральному числу N выведите такое
# наименьшее целое число k, что 2ᵏ≥N.
# Операцией возведения в степень пользоваться нельзя!
n = int(input())
k = 1
m = 0
while k < n:
    k = k * 2
    m = m + 1
print(m)
>>>>>>> 269de5d41663c4fb0349d6313bbb4fb81b0aae7a
