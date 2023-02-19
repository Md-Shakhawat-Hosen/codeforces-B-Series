t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    one = 0
    sum = 0
    for i in li:
        if i == 1:
            one = one + 1
            sum = sum + 1
        else:
            sum = sum + 2
    if sum % 2 == 0:
        d = int(sum/2)
        if d % 2 == 0:
            print("YES")
        else:
            if one:
                print("YES")
            else:
                print("NO")
    else:
        print("NO")

