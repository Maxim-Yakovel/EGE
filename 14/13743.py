f = 49**10 + 7**30 - 49
s = ''
while f > 0:
    s = str(f % 7) + s
    f = f // 7
print(s)
