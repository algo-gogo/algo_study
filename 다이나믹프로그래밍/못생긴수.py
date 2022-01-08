n = int(input())

d = [0] * n

print(d)

num2 = 2
num3 = 3
num5 = 5

mul2 = 1
mul3 = 1
mul5 = 1

d[0] = 1
for i in range(1, n):

    d[i] = min(num2 * mul2, num3 * mul3, num5 * mul5)
    if d[i] == num2 * mul2:
        mul2 += 1
    if d[i] == num3 * mul3:
        mul3 += 1
    if d[i] == num5 * mul5:
        mul5 += 1

print(d)
print(d[n - 1])