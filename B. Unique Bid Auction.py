t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    li3 = li.copy()
    li3 = list(set(li3))
    li3.sort()
    value = 0
    flag = False
    for i in range(len(li3)):
        c = li.count(li3[i])
        if c == 1:
            value = li3[i]
            flag = True
            break

    if flag:
        print(li.index(value) + 1)
    else:
        print(-1)







