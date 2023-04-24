import itertools
f = itertools.product('METRO', repeat=4)
count = 0
for x in f:
    l = ''.join(x)
    if l[0] in ['M', 'T', 'R'] and l[-1] in ['E', 'O']:
        count += 1
print(count)