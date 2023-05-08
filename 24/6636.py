f = open('24_6636 (1).txt')
nums = f.read()
count = 0
i = 0
m = 0
while i < (len(nums) - 1):
    if int(nums[i]) % 2 == 0 and int(nums[i + 1]) % 2 != 0:
        count += 1
        i += 2
        m = max(count, m)
    else:
        count = 0
        i += 1
print(m)
