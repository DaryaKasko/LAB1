print("Введите числа: ")
a = float(input(print("a = ")))
b = float(input(print("b = ")))
c = float(input(print("c = ")))

if (a == b and c != b) or (a == c and b != a) or (b == c and b != a):
    print("Два числа равны между собой")
elif a == b and b == c:
    print("Все три числа равны между собой")
else:
    print("Нет равных между собой чисел")