def toZero(N):
    i = N
    while i > 0:
        yield i
        i= i-1

n = int(input("Numbers to zero from: "))
for i in toZero(n):
    print(i)


