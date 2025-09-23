n = int(input("Введите количество разрядов: "))

mid = (n + 1) // 2

result = []
for i in range(1, mid + 1):
    result.append(i)

for i in range(mid - 1, 0, -1):
    result.append(i)

print(''.join(map(str, result)))