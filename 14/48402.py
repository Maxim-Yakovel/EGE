for x in range(10):
    res = int(f'3{x}DA', 14) + int(f'5{x}A6', 12)
    if res % 81 == 0:
        print(res // 81)
        break
