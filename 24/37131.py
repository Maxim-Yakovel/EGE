f = open('24 (1).txt')
num = f.read()
count = 1
for i in range(len(num)):
    if num[i-1:i+1] not in ['KL' and 'LK']:
        count += 1
    else:
        count = 1
print(count)