f = open('17 (5).txt')
num = list (map(int, f.readlines()))
count = m = 0
for i in range(len(num) - 1):
    for n in range(i+1, len(num)):
         if (num[i] * num[n]) % 26 == 0:
             count += 1
             m = max(num[i] + num[n], m)
print(count, m)
