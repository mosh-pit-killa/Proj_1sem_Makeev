from math import sqrt

a = 7
b = 2
c = 8

def triangle_perimeter(a1=a, b1=b, c1=c):
    return a1 + b1 + c1

def triangle_area(a1=a, b1=b, c1=c):
    p = (a1 + b1 + c1) / 2
    return sqrt(p * (p - a1) * (p - b1) * (p - c1))
