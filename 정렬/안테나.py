n = int(input())
numList = list(map(int, input().split()))

numList.sort()

print(numList)
#
# resultList = []
# for i in range(len(numList)):
#     result = 0
#     for j in range(len(numList)):
#         result += abs(numList[i] - numList[j])
#     resultList.append(result)
#
# print(resultList)
# print(min(resultList))

# resultList = [0] * n
# for i in range(len(numList)):
#     resultList[i] = sum(numList) - n * numList[i]
#
# print(resultList)
# print(min(resultList))

avgNum = sum(numList) // len(numList)
resultList = []
for i in numList:
    resultList.append((abs(avgNum - i), i))

print(resultList)
print(min(resultList)[1])