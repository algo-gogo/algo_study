n, k = map(int, input().split())


arr = []
for i in range(0, n):
    arr.append(int(input()))

arr.sort(reverse=True)
print(arr)

result = 0
for i in arr:
    if k // i != 0:
        result +=k // i
        k = k % i

print(result)