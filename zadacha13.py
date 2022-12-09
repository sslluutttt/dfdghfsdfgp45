from math import sqrt

a = int(input())
b = int(input())
c = int(input())

v = a * b * c
d = sqrt(a ** 2 + b ** 2 + c ** 2)
print('Объём параллелепипеда равен:', v)
print('Длина большой диагонали равна: ', d)