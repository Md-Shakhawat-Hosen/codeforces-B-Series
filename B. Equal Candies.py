t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    if n == 1:
        print(0)
    else:
        s = min(li)
        c = 0
        for i in range(n):
            c = c + abs(li[i] - s)
        print(c)
