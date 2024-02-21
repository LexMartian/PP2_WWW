def divisible3_4(N):
    i = 0
    while i < N:
        yield i
        i += 12

n = int(input("Even numbers until: "))
for i in divisible3_4(n):
    print(i)

