f = open('17 (6).txt')
nums = list(map(int, f.readlines()))
count = m = 0
for i in range(len(nums)):
    for n in range(i + 1, len(nums)):
        if (nums[i] - nums[n]) % 60 == 0 and (nums[i] % 15 == 0 or nums[n] % 15 == 0):
            count += 1
            m = max(nums[i] - nums[n], m)
print(count, m)