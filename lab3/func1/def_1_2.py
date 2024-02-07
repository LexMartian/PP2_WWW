def toOunces(grams):
    print(28.3495231 * grams)

weight = float(input("Input the weight in gramms: "))
ounces = toOunces(weight)

def toCelsius(fh):
    print((5/9) * (fh - 32))

C = float(input("Input the temperature in Celsius: "))
Faren = toCelsius(C)