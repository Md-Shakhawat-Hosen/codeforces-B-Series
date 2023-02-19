t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    li1 = list(set(li))
    ind = -1
    for i in range(len(li1)):
        r = li.count(li1[i])
        if r >= 3:
            ind = li1[i]
            break
    if ind == -1:
        print(-1)
    else:
        print(ind)
    li.clear()
    li1.clear()