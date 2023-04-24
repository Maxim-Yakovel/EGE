f = open('17 (3).txt')
num = list(map(int, f.readlines()))
count = m = 0
for i in range(len(num) - 1):
    if (num[i] % 3 == 0 or num[i + 1] % 3 == 0) and ((num[i] + num[i + 1]) % 5 == 0):
        count += 1
        m = max(num[i] + num[i + 1], m)
print(count, m)
