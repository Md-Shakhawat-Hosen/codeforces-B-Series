t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    li.sort()
    c = abs(li[0]-li[1])
    if len(li) == 2:
        print(abs(li[0]-li[1]))
    else:
        for j in range(n - 1):
            if abs(li[j] - li[j + 1]) < c:
                c = abs(li[j] - li[j + 1])
        print(c)

