f = open('40733.txt')
num = list(map(int, f.readlines()))
count = m = 0

avg = 0
for i in range(len(num)):
    if num[i] % 2 == 0:
        count += 1
        avg += num[i]
avg = avg / count
count1 = 0
for i in range(len(num) - 1):
    if (num[i] % 3 == 0 or num[i + 1] % 3 == 0) and (num[i + 1] < avg or num[i] < avg):
        count1 += 1
        m = max(m, num[i] + num[i + 1])
print(count1, m)



