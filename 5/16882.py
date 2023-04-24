for n in range(256):
    num = bin(n)[2:]
    num = str(num)
    num = '0'*(8 - len(num)) + num
    num = num.replace('1', '*')
    num = num.replace('0', '1')
    num = num.replace('*', '0')
    d = int(num, 2) - int(n)
    if d == 111:
        print(n)
#я не сам додумался, посмотрел решение на решуегэ, честно говоря я в шоке
