import itertools
f = itertools.product('12345', repeat=5)
count = 0
for x in f:
    zxc = ''.join(x)
    if zxc.count('1') == 3:
        count += 1
print(count)