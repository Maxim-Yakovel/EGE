import itertools
f = itertools.product('ЛЕВИЙ', repeat=5)
count = 0
for x in f:
    l = ''.join(x)
    if l[0] != 'Й' and l.count('ЕИ') == 0 and l.count('Л') == 1 and l.count('Е') == 1 and l.count('В') == 1 and l.count('И') == 1 and l.count('Й') == 1:
        count += 1
print(count)