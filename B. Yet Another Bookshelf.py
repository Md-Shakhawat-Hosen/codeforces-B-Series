t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]

    first_index = li.index(1)
    last_index = 0
    for i in range(len(li)-1,0,-1):
        if li[i] == 1:
            last_index = i
            break
    c = 0
    for i in range(first_index,last_index+1):
        if li[i] == 0:
            c = c + 1

    print(c)
