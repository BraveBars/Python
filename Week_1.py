''' # 100A
print("A" * 100)

# Пингвины.
N = int(input())
print('   _~_    ' * N)
print('  (o o)   ' * N)
print(' /  V  \  ' * N)
print('/(  _  )\ ' * N)
print('  ^^ ^^   ' * N)

# Сумма цифр трехзначного числа
n = int(input())
a = n // 100
b = (n - (n // 100 * 100)) // 10
c = n - n // 10 * 10
print(a + b + c)

# Стоимость покупки. Пирожок в столовой стоит A рублей и B копеек.
# Определите, сколько рублей и копеек нужно заплатить за N пирожков.
A = int(input())
B = int(input())
N = int(input())
C = A * 100 + B
T = C * N
print(T // 100, T % 100)

# Электронные часы-1.
N = int(input())
M = 60 * 24
H = (M + N)
print(H // 60 % 24, H % 60)

# Следующее и предыдущее.
N = int(input())
NN = N + 1
PN = N - 1
print("The next number for the number ", N, " is ", NN, ".", sep="")
print("The previous number for the number ", N, " is ", PN, ".", sep="")

# 100 раз подряд в квадрате. Заданное число N записали 100 раз подряд и
# затем возвели в квадрат. Что получилось?'''
N = int(input())
print(int(str(N) * 100) ** 2)