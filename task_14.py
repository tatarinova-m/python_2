# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

N = int(input("Введите число N: "))
list = []
x = 2
while x < N:
    list.append(x)
    x *=2
print(list)