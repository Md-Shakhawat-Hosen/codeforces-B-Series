t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    m = li[-1]
    c = 0
    for i in range(n-2,-1,-1):
        if li[i] > m:
            c = c + 1
        m = min(li[i],m)

    print(c)



