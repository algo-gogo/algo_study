# from itertools import combinations
#
# n, c = map(int, input().split())
#
# nList = []
# for i in range(n):
#     nList.append(int(input()))
#
# nList.sort()
#
# print(nList)
#
# selectN = list(combinations(nList, 3))
# print(selectN)
#
# resultList = []
# for n1, n2, n3 in selectN:
#     result = 0
#     resultList.append(min(abs(n1 - n2), abs(n2 - n3)))
#
# print(max(resultList))

# ---------------------------------------------------------
n, c = map(int, input().split())

nList = []
for i in range(n):
    nList.append(int(input()))

nList.sort()

print(nList)

def binarySearch(array, start, end):
    while start <= end:
        mid = (start + end) // 2

    return False
