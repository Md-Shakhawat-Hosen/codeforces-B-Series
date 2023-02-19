t = int(input())
for i in range(t):
    n = int(input())
    i = 1
    li = []
    while True:
        if i*i <= n:
            li.append(i*i)

        if i*i*i <= n:
            li.append(i*i*i)
        if i*i > n:
            break
        i = i + 1
    print(len(set(li)))