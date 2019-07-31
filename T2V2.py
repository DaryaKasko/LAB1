import numpy
import math
a = 0.002
b = 8.5
n = 2

for i in [2, 1, 8, 3]:
    y = math.sqrt(i * b - b ** 2 * a)
    z = y * math.tan(n / 4) - math.exp(1 + b)
    print(y, z)

print("\n")

i = 1
while i < 4:
    y = math.sqrt(i * b - b ** 2 * a)
    z = y * math.tan(n / 4) - math.exp(1 + b)
    i += 0.5
    print(y, z)

print("\n")

b = 2
while b < 4:
    for n in [3, -6, 0.2, 2.8]:
        y = math.sqrt(i * b - b ** 2 * a)
        z = y * math.tan(n / 4) - math.exp(1 + b)
        print(y, z)
    b += 0.5