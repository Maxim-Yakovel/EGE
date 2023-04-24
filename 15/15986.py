for a in range(64):
    f = True
    for x in range(64):
        for y in range(64):
            if not ((y + 2 * x != 48) or (a < x) or (x < y)):
                f = False
    if f:
        print(a)
