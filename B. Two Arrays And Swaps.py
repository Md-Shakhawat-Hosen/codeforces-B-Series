t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))[:n]
    b = list(map(int, input().split()))[:n]
    a.sort()
    b.sort()
    b.reverse()
    s = 0
    if k == n:
        for j in range(k):
            if a[j] >= b[j]:
                s = s + a[j]
            else:
                s = s + b[j]
        print(s)
    elif k == 0:
        a_sum = sum(a)
        print(a_sum)
    else:
        s1 = 0
        for j in range(k):
            if a[j] >= b[j]:
                s = s + a[j]
            else:
                s = s + b[j]
        for i in range(k,n):
            s1 = s1 + a[i]
        print(s+s1)

