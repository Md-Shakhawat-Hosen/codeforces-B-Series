t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:2*n]
    new = set(li)
    for i in new:
        print(i,end =" ")
    print()