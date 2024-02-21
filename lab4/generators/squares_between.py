def squares(a, b):
    i = int(a ** 0.5) + 1
    while i ** 2 <= b:
        yield i ** 2
        i += 1

# Test the generator with a for loop
a = int(input("Squares from: "))
b = int(input("to "))

print("Squares between", a, "and", b, "are:")
for square in squares(a, b):
    print(square)

