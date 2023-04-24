f = open('39246.txt')
num = list(map(int, f.readlines()))

count = m = 0
for i in range(len(num) - 1):
    if (num[i] % 5 == 0 or num[i + 1] % 5 == 0) and ((num[i] + num[i + 1]) % 7 == 0):
        count += 1
        m = max(m, num[i] + num[i + 1])
print(count, m)