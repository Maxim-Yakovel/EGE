f = open('24_demo.txt')
num = f.read()
i = 0
count = 1
m = 0
while i < len(num) - 1:
    if num[i] != num[i+1]:
        count += 1
        i += 1
        m = max(count, m)
    else:
        count = 1
        i += 1
print(m)
    