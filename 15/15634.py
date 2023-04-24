for a in range(1, 150):
    f = True
    for x in range(1, 150):
        for y in range(1, 150):
            s = (y + 2 * x < a) or (x > 30) or (y > 20)
            if s == 0:
                f = False
    if f:
        print(a)
        break