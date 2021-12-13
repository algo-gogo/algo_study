# https://www.acmicpc.net/problem/1715

n = int(input())
nList = []
for i in range(n):
    a = int(input())
    nList.append(a)

nList.sort()

print(nList)
# result = 0
# length = len(nList)
# for i in range(length - 1):
#     nList[i + 1] = nList[i] + nList[i + 1]
#     result += nList[i + 1]
#
# print(result)

result = 0
length = len(nList)
sumN = 0
for i in range(length - 1):
    sumN = nList[0] + nList[1]
    del nList[0]
    del nList[0]
    nList.append(sumN)
    result += sumN
    nList.sort()

print(result)