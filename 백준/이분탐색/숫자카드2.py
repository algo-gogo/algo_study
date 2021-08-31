# import sys
#
# n = sys.stdin.readline().rstrip()
# nList = list(map(int, sys.stdin.readline().rstrip().split()))
# m = sys.stdin.readline().rstrip()
# mList = list(map(int, sys.stdin.readline().rstrip().split()))
# resultDic = {}
#
# for i in mList:
#     resultDic[i] = 0
#
# for i in nList:
#     if i in resultDic:
#         resultDic[i] += 1
#
# for i in resultDic:
#     print(resultDic[i], end=' ')

n = int(input())
arr1 = list(map(int, input().split()))
dict1 = dict()
for i in arr1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
m = int(input())
arr2 = list(map(int, input().split()))
for i in arr2:
    if i in dict1:
        print(dict1[i], end=' ')
    else:
        print(0, end=' ')
