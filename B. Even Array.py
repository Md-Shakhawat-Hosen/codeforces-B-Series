t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    odd = 0
    even = 0
    for i in range(len(li)):
        if i % 2 == 0 and li[i] % 2 != 0:
            even = even + 1
        elif i % 2 != 0 and li[i] % 2 == 0:
            odd = odd + 1

    if (even != 0 and odd != 0) and even == odd:
        print(even)
    elif even == 0 and odd == 0:
        print(0)
    else:
        print(-1)




