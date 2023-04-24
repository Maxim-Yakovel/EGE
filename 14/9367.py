f = 9**8 + 3**5 - 9
s = ''
while f > 0:
    s = str(f % 3) + s
    f = f//3
print(s.count('2'))
