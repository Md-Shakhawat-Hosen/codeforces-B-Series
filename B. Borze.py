s = input()
li = []
i = 0
while i < len(s):
    if s[i] == '-':
        t = i + 1
        if t > len(s):
            break
        else:

            if s[t] == '.':
                li.append(1)
                i = i + 2
            elif s[t] == '-':
                li.append(2)
                i = i + 2
    else:
        li.append(0)
        i = i + 1

for i in li:
    print(i,end="")


