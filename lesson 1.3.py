# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n = int(input('Введите число: '))

a = str(n)
b = str(n)+str(n)
c = str(n)+str(n)+str(n)
result = int(a) + int(b) + int(c)

print(result)


