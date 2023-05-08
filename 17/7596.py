f = open('17_7596.txt')
num = list(map(int, f.readlines()))
mmin = 100000
m = 10000000
count = 0
for i in range(len(num)):
    if 99 < num[i] < 1000 and str(num[i])[-1] == '5':
        mmin = min(mmin, num[i])
for i in range(len(num) - 1):
    if ((99 < num[i] < 1000 and num[i + 1] not in range(100, 1000)) or (99 < num[i + 1] < 1000 and num[i] not in range(100, 1000))) and ((num[i] + num[i + 1]) % mmin == 0):
        count += 1
        m = min(num[i] + num[i + 1], m)
print(count, m)
