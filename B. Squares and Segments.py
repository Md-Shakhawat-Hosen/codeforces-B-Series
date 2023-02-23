import math
n = int(input())
b = int(math.sqrt(n))
a = b
if math.sqrt(n) != b:
    b = b + 1
if a*b < n:
    a = a + 1

print(a+b)