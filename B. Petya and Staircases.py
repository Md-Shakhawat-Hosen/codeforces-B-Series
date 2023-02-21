n,m = map(int,input().split())
if m == 0:
    print("YES")
else:
    li = list(map(int, input().split()))[:m]
    li.sort()
    flag = False
    if li[0] == 1 or li[m - 1] == n:
        flag = True

    c = 1
    for i in range(m-1):
        if li[i + 1] - li[i] == 1:
            c = c + 1
            if c == 3:
                flag = True
                break
        else:
            c = 1
    if flag:
        print("NO")
    else:
        print("YES")



