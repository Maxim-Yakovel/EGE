import itertools
s = itertools.product('1234', repeat=5)
count = 0
for str in s:
    line = ''.join(str)
    if line.count('1') == 2:
        count += 1
print(count)