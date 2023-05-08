f = open('17 (7).txt')
num = list(map(int, f.readlines()))
count = m = 0
for i in range(len(num) - 1):
    for n in range(i + 1, len(num)):
        if (num[i] % 160 != num[n] % 160) and ((num[i] % 7 == 0) or (num[n] % 7 == 0)):
            count += 1
            m = max(m, num[i] + num[n])
print(count, m)
