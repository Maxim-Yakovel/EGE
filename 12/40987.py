for i in range(201, 500):
    s='1'*i
    while '1111' in s:
        s=s.replace('1111', '22', 1)
        s=s.replace('222', '1', 1)
    if s.count('1')==0:
        print(i)
        break