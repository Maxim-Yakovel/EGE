f = open('17 (4).txt')
num = list(map(int, f.readlines()))
count = m = 0
for i in range(len(num) - 1):
    if (num[i] + num[i + 1]) % 117 == 0:
        count += 1
        m = max(num[i] + num[i + 1], m)
print(count, m)
