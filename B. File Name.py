n = int(input())
s = input()[:n]
c = 1
m = 0
t = 0
for i in range(len(s)-1):
    if s[i] == s[i+1] == 'x':
        c = c + 1
    else:
        if c >= 3:
            m = c
            t = t + (m-2)
        c = 1

if c:
    if c >= 3:
        print(t+(c-2))
    else:
        print(t)
else:
    print(0)