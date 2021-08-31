# n = int(input())
# nList = list(map(int, input().split()))
# m = int(input())
# mList = list(map(int, input().split()))
#
#
# def binarySearch(target, data):
#     data.sort()
#     start = 0
#     end = len(data) - 1
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if data[mid] == target:
#             return data[mid]
#         elif data[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return None
#
#
# for i in mList:
#     search = binarySearch(i, nList)
#     if i == search:
#         print('1')
#     else:
#         print('0')

import sys

n = sys.stdin.readline().rstrip()
nList = list(map(int, sys.stdin.readline().rstrip().split()))
nList.sort()
m = sys.stdin.readline().rstrip()
mList = list(map(int, sys.stdin.readline().rstrip().split()))


def binary_search(element, list, start=0, end=None):
    if end == None:
        end = len(list) - 1
    if start > end:
        return 0

    mid = (start + end) // 2
    if element == list[mid]:
        return 1
    elif element < list[mid]:
        end = mid - 1
    else:
        start = mid + 1
    return binary_search(element, list, start, end)


for i in mList:
    print(binary_search(i, nList))
