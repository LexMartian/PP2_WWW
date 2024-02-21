import math

def toRad(degree):
    return degree / 180 * math.pi

#degree = float(input("Enter degrees: "))
#print(toRad(degree))

def areaTrap(h, a, b):
    return (a+b)/2 * h

#print(areaTrap(5, 5, 6))

def areaPoly(n, l):
    if n <= 2:
        return 0
    if n == 3:
        return sqrt(3) * l**2 / 4
    if n == 4:
        return l**2
    if n == 5:
        return sqrt(5* (5 + 2*sqrt(5))) * l**2 / 4
    if n == 6:
        return 3 * sqrt(3) * l**2 / 2
    if n > 6:
        apothem = l / (2* (math.tan(180/n)))
        return n * l * apothem /2
#print(areaPoly(4, 25))

def areaParall(l, h):
    return h*l
#print(areaParall(6, 5))