t = input()
li = []
s1 = []
s2 = []
for i in t:
    if i != 'a':
        li.append(i)

if len(li) == 0:
    print(t)
elif len(li) != 0 and t[len(t)-1] == 'a':
    print(":(")
elif len(li) % 2 == 0:
    half = int(len(li) / 2)
    for i in range(len(li)):
        if i < half:
            s1.append(li[i])
        else:
            s2.append(li[i])

    if s1 == s2:
        for i in range(len(t)-half):
            print(t[i],end="")
    else:
        print(":(")
else:
    print(":(")

