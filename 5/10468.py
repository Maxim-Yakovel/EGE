for n in range(100):
    r = bin(n)[2:]
    for i in range(2):
        c = r.count('1')
        r += str(c % 2)
    if int(r, 2) > 77:
        print(n)
        break