f = open('17 (1).txt')
nums = list(map(int, f.readlines()))
count = m = 0
for i in range(len(nums) - 1):
    if nums[i] % 3 == 0 or nums[i + 1] % 3 == 0:
        count += 1
        m = max(nums[i] + nums[i + 1], m)
print(count, m)