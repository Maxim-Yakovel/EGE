from fnmatch import fnmatch
for n in range(0, 10 ** 10, 2023):
    if fnmatch(str(n), '1?2139*4'):
        print(n)
        print(n / 2023)