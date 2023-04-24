f = open('24.txt')
str = f.read()
count = 1
m = 0
for i in range(1, len(str)):
    if str[i-1:i+1] not in ['ad', 'da']:
        count += 1
    else:
        count = 1
    m = max(m, count)
print(m)