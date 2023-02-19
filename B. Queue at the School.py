n,t = map(int,input().split())
st = input()
s = list(st)

for i in range(t):
    j = 0
    while j < len(s)-1:
        if s[j] == 'B':
            if s[j + 1] == 'G' and j < len(s):
                temp = s[j+1]
                s[j+1] = s[j]
                s[j] = temp
                j = j + 2
            else:
                j = j + 1
        else:
            j = j + 1

for i in s:
    print(i,end="")
