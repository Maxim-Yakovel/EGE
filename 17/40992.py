f = open('17 (40992).txt')
num = list(map(int, f.readlines()))
count = count1 = avg = m = 0
for i in range(len(num) - 1):
    if num[i] % 2 != 0:
        count1 += 1
        avg += num[i]
avg = avg / count1
for i in range(len(num) - 1):
    if (num[i] % 5 == 0 or num[i + 1] % 5 == 0) and (num[i] < avg or num[i + 1] < avg):
        count += 1
        m = max(m, num[i] + num[i + 1])
print(count, m)
