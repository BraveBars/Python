# 100A
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