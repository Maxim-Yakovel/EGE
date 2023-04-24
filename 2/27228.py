print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (not(x) or y or z) == (not(y) and z and w)
                if f == 1:
                    print(y, w, z, x)
