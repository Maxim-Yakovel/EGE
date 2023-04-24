import itertools
f = itertools.product('abcdxy', repeat=4)
count = 0
for x in f:
    l = ''.join(x)
    if l[0] == 'x' and l.count('x') == 1 and l.count('y') == 0 or l[0] == 'y' and l.count('y') == 1 and l.count('x') == 0:
        count += 1
print(count)