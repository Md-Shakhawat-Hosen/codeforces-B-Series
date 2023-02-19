T = int(input())
for x in range(T):
    size = int(input())
    li = list(map(int,input().split()))[:size]
    myset = set(li)
    if len(li) != len(myset):
        print("NO")
    else:
        print("YES")
