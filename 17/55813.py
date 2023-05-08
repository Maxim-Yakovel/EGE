f = open('17 (8).txt')
num = list(map(int, f.readlines()))
min5 = 100000
count = 0
m = 1000000
for i in range(len(num)):
    if num[i] >= 100 and num[i] < 1000 and str(num[i])[-1] == '5':
        min5 = min(num[i], min5)
for i in range(len(num) - 1):
    if (((num[i] > 99 and num[i] < 1000) and (num[i + 1] < 100 or num[i + 1] > 999)) or ((num[i + 1] > 99 and num[i + 1] < 1000) and (num[i] < 100 or num[i] > 999))) and ((num[i] + num[i+1]) % min5):
        count += 1
        m = min(num[i] + num[i+1], m)
print(count, m)
