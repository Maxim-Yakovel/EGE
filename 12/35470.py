for i1 in range(1, 100):
    for i2 in range(1, 100):
        for i3 in range(1, 100):
            s = '0' + '1' * i1 + '2' * i2 + '3' * i3
            while ('01' in s) or ('02' in s) or ('03' in s):
                s = s.replace('01', '2302', 1)
                s = s.replace('02', '10', 1)
                s = s.replace('03', '201', 1)
            if s.count('1') == 40 and s.count('2') == 10 and s.count('3') == 8:
                print(i1)