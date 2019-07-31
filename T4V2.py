import random

n = int(input(print("Введите размер списка: \n")))
A = []
for i in range(n):
    a = random.randint(1, 100)
    A.append(a)
print("Список чисел: ", A)

B = []
for j in A:
    if j % 2 == 0:
        B.append(j)
print("Четные числа из списка: ", B)