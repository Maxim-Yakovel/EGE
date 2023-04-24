print('x z y')
for x in range(2):
    for y in range(2):
        for z in range(2):
            f =  (x or y) <= (z == x)
            if f == 0:
                print(x, z, y)