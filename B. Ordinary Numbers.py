t = int(input())
for i in range(t):
    n = int(input())
    c = 0
    for i in range(1,10):
        start = i
        while start <= n:
            c = c + 1
            start = start*10 + i
    print(c)
