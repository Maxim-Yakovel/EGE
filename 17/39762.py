# открытие файла для чтения
f = open('39762.txt')
# list() - преобразование чего-либо к списку
# map(<функция>, <коллекция>) - функция, применяющая к каждому элементу коллекции какую-либо функцию
# В нашем случае, каждый элемент преобразуется из строки в число при помощи функции int
nums = list(map(int, f.readlines()))
count = m = 0
# len(<массив>) - длина массива
for i in range(len(nums) - 1):
    if (nums[i] * nums[i + 1]) % 15 == 0 and (nums[i] + nums[i + 1]) % 7 == 0:
        count += 1
        m = max(m, nums[i] + nums[i + 1])
print(count, m)
