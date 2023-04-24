for a in range(64):
    f = True
    for x in range(64):
        if not ((x & 41 != 0) <= ((x & 33 == 0) <= (x & a != 0))):
            f = False
    if f:
        print(a)
        break
