for n in range(49):
    r = bin(n)[2:]
    for i in range(2):
        c = r.count('1')
        r += str(c % 2)
    if int(r, 2) > 85:
        print(n)
        break