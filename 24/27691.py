f = open('zadanie24_1.txt')
str = f.read()
count = 1
m = 0
for i in range(len(str)):
    if str[i] == 'A' and str[i + 1] == 'A':
        count += 1
    else:
        count = 1
    m = max(m, count)
print(m)
