count = 0
for a in range(1, 200):
    f = True
    for x in range(1, 200):
        for y in range(1, 200):
            s = ((x < 6) <= (x**2 < a)) and ((y**2 <= a) <= (y <= 6))
            if s == 0:
                f = False
    if f:
        count += 1
print(count)