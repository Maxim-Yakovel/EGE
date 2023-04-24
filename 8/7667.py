import itertools
f = itertools.product('ЕГЭ', repeat=5)
count = 0
for str in f:
    line = ''.join(str)
    if line[0] != 'Г':
        count += 1
print(count)