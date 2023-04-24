f = open('24 (2).txt')
num = f.read()
count = 0
i = 0
m = 0
while i < len(num):
    if num[i:i+2] in ['CO', 'CA', 'DO', 'DA', 'FO', 'FA']:
        i += 2
        count += 1
        m = max(count, m)
    else:
        i += 1
        count = 0
print(m)