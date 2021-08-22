cityNum = int(input())

distance = list(map(int, input().split()))

price = list(map(int, input().split()))

# distanceSum = 0
# for i in distance:
#     distanceSum += i
#
# print(distanceSum)
#
# minPrice = price[0]
# minIndex = 0
# for i in range(0, len(price) - 1):
#     if minPrice >= price[i]:
#         minPrice = price[i]
#         minIndex = i
#
# print(minPrice)
# print(minIndex)

# result = 0
# for i in range(0, minIndex):
#     result += price[i] * distance[i]
#     distanceSum -= distance[i]
#
# result += distanceSum * minPrice

# print(result)

minPrice = price[0]
result = 0
for i in range(0, len(price) - 1):
    if minPrice >= price[i]:
        minPrice = price[i]
    result += minPrice * distance[i]

print(result)
