
# 1 - 집
# 2 - 치킨집


def twoListSelect(twoList, b):
    if len(twoList) == b:
        return twoList
    # 폐업해야하는 가게 찾기...

a, b = map(int, input().split())

array = []
for i in range(a):
    aa = list(map(int, input().split()))
    array.append(aa)

oneList = []
twoList = []
print(array)
for i in range(a):
    for j in range(a):
        if array[i][j] == 1:
            oneList.append((i, j))
        if array[i][j] == 2:
            twoList.append((i, j))

print(oneList)
print(twoList)
twoListSelect(twoList, b)
distanceList = []
resultList = []
for a, b in twoList:
    for x, y in oneList:
        distance = abs(a - x) + abs(b - y)
        distanceList.append(distance)
    resultList.append(min(distanceList))
    distanceList = []
print(resultList)
resultList.sort()
print(resultList)
result = sum(resultList[:b])
print(result)

