t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    l1 = set(li)
    print(len(l1))