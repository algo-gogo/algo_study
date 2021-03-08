# 백준 -> ATM

n = int(input())

# 3 1 4 3 2
array = list(map(int, input().split()))

# 1 2 3 3 4
array.sort()

result = 0

for i in range(n):
    for j in range(i+1):
        result += array[j]


print(result)