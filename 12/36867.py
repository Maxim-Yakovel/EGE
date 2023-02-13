for i1 in range(1, 100):
    for i2 in range(1, 100):
        for i3 in range(1, 100):
            s = '0' + '1' * i1 + '2' * i2 + '3' * i3 + '0'
            while '00' not in s:
                s=s.replace('01','210',1)
                s=s.replace('02','320',1)
                s=s.replace('03','3012',1)
            if s.count('1')==26 and s.count('2')==54 and s.count('3')==48:
                print(i1+i2+i3+2)
