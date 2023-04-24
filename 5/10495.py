for n in range(1, 200):
    r = bin(n)[2:]
    a = r.count('1')
    r = r + str(a % 2)
    b = r.count('1')
    r = r + str(b % 2)
    if int(r, 2) > 97:
        print(n)
        break