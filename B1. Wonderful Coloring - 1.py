t = int(input())
for i in range(t):
    s = input()
    li = list(s)
    li1 = list(set(li))
    d = 0

    for i in range(len(li1)):
        c = li.count(li1[i])
        if c > 2:
            d = d + 2
        else:
            d = d + c

    r = d // 2
    print(r)
