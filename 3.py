c = 3
a = 2
b = 10
while b > a:
    a += c
    b -= 1
    c += 1
if a >= b:
    c *= b
print(c)