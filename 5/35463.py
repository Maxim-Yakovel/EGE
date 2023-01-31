for num in range(100, 1000):
    # Убираем с помощью среза 2 первых символа
    b = bin(num)[2:]
    for i in range(3):
        count0 = b.count('0')
        count1 = b.count('1')
        if count0 == count1:
            b += b[-1]
        else:
            if count0 > count1:
                b += '1'
            else:
                b += '0'
    # int(строка, система счисления ИЗ которой переводим)
    if int(b, 2) % 4 == 0:
        print(num)
        break
