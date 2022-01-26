x = 3
y = 0
while x >= 0:
    if x > y:
        y = x * x
        break
    y = x - 1
else:
    y = x
print(y)

