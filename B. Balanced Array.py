t = int(input())
for i in range(t):
    li = []
    n = int(input())
    r = n // 2
    if r % 2 == 0 and n % 2 == 0:
        i = 0
        j = 2
        while i < r:
            li.append(j)
            i = i + 1
            j = j + 2
        re = sum(li)
        k = 1
        odd_sum = 0
        while r < n - 1:
            odd_sum = odd_sum + k
            li.append(k)
            r = r + 1
            k = k + 2

        total = re - odd_sum
        li.append(total)
        print("YES")
        for i in li:
            print(i,end=" ")
        print()
    else:
        print("NO")


