def squares(N):
    i = 1
    while i**2 <= N:
        yield i**2
        i += 1

n = int(input("Generate squares until: "))
for i in squares(n):
    print(i)