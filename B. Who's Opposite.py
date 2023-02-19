t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    n = a + b
    if n % 2 == 0:
        half = n // 2
        li = []
        li1 = []
        for i in range(1,half+1):
            li.append(i)
        for j in range(half+1,n+1):
            li1.append(j)
        if a > b:
            ind_1 = li.index(b)
            ind_2 = li1.index(a)
        else:
            ind_1 = li.index(a)
            ind_2 = li1.index(b)

        if ind_1 == ind_2:
            if c <= half:
                ind = li.index(c)
                print(li1[ind])
            else:
                ind = li1.index(c)
                print(li[ind])
        else:
            print(-1)
    else:
        n = n - 1
        half = n // 2
        li = []
        li1 = []
        for i in range(1, half + 1):
            li.append(i)
        for j in range(half + 1, n + 1):
            li1.append(j)
        if a > b:
            ind_1 = li.index(b)
            ind_2 = li1.index(a)
        else:
            ind_1 = li.index(a)
            ind_2 = li1.index(b)

        if ind_1 == ind_2:
            if c <= half:
                ind = li.index(c)
                print(li1[ind])
            else:
                ind = li1.index(c)
                print(li[ind])
        else:
            print(-1)