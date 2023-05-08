f = open('24_7600.txt')
num = f.read()
h = ['Q', 'R', 'S']
i = 0
m = 0
count = 1
while i < len(num) - 1:
    if (num[i] not in h) or (num[i + 1] not in h):
        count += 1
        i += 1
        m = max(count, m)
    else:
        count = 1
        i += 1
print(m)