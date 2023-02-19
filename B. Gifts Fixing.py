t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))[:n]
    b = list(map(int,input().split()))[:n]
    min_a = min(a)
    min_b = min(b)
    total = 0
    for j in range(n):
        d1 = abs(min_a - a[j])
        d2 = abs(min_b - b[j])
        total = total + max(d1,d2)

    print(total)
