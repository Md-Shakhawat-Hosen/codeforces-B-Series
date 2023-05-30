t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    count = 0
    ans = 0
    for i in range(n):
        count = count + 1
        if i == n-1 or s[i] != s[i+1]:
            ans = max(ans,count)
            count = 0

    print(ans+1)