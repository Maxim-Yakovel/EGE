for n in range(1, 50):
    r = bin(n)[2:]
    if r[-1] == '0':
        r = r + '01'
    else:
        r = r + '10'
    if int(r, 2) > 102:
        print(int(r, 2))
        break