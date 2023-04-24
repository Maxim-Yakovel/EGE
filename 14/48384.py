for x in range(10):
    for y in range(10):
        r = int(f'8{x}78{y}', 13) + int(f'79{x}{y}7', 18)
        if r % 9 == 0:
            print(r // 9)
            break