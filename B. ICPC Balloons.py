t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    li = set(s)
    r = n - len(li)
    print(2*len(li)+r)