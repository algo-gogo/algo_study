# 4 11
# 802
# 743
# 457
# 539

k, n = map(int, input().split())

kList = []
for i in range(k):
    kList.append(int(input()))

start, end = 1, max(kList)

# print(kList)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in kList:
        lines += i // mid
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
