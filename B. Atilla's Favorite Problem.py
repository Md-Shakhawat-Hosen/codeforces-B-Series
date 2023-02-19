
t = int(input())
ch = 'a'
for i in range(t):
    n = int(input())
    s = input()[:n]
    r = max(s)
    print((ord(r)-ord(ch))+1)
