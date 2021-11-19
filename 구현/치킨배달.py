
# 1 - 집
# 2 - 치킨집

from itertools import combinations

a, b = map(int, input().split())

array = []
for i in range(a):
    aa = list(map(int, input().split()))
    array.append(aa)

# 1 - 집
houseList = []
# 2 - 치킨
chickenList = []
print(array)
for i in range(a):
    for j in range(a):
        if array[i][j] == 1:
            houseList.append((i, j))
        if array[i][j] == 2:
            chickenList.append((i, j))

print("house", houseList)
print("chicken", chickenList)
chickenListSelect = list(combinations(chickenList, b))

print("chickenListSelect", chickenListSelect)

resultList = [[0] for i in range(len(chickenListSelect))]
print("resultList", resultList)
for house in houseList:
    for chickenSelect in range(len(chickenListSelect)):
        distanceList = []
        for i in range(b):
            distance = abs(house[0] - chickenListSelect[chickenSelect][i][0]) + abs(house[1] - chickenListSelect[chickenSelect][i][1])
            distanceList.append(distance)
        chickenDistance = min(distanceList)
        resultList[chickenSelect].append(chickenDistance)

print(resultList)
minList = []
for i in resultList:
    minList.append(sum(i))

print(min(minList))
