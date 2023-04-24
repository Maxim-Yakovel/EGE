import itertools
f = itertools.product('ABCX', repeat=5)
count = 0
for x in f:
    line = ''.join(x)
    if line.count('X') == 1 and line[4] == 'X' or line.count('X') == 0:
        count += 1
print(count)