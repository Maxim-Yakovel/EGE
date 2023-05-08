# Ускоренный способ получения делителей числа
def div_count(n):
    divs = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return divs

count = 0
num = 300000001
while count < 5:
    divs = sorted(div_count(num))
    if len(divs) >= 5:
        print(divs[-5])
        count += 1
    num += 1
