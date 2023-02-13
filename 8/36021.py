import itertools
strings = itertools.product('ВИШНЯ', repeat=6)
count = 0
for str in strings:
    line = ''.join(str)
    if line.count('В')<=1 and line[0]!='Ш' and line[5] not in 'ИЯ':
        count+=1
print(count)

