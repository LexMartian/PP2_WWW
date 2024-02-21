def evens(N):
    i = 0
    while i < N:
        yield i
        i += 2

n = int(input("Even numbers until: "))
for i in evens(n):
    print(i)
