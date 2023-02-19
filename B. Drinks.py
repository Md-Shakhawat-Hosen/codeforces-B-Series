n = int(input())
li = list(map(int,input().split()))[:n]
s = sum(li)
r = s / n
print("{:.12f}".format(r))


