# n = int(input())
# nList = list(map(int, input().split()))
# m = int(input())
# mList = list(map(int, input().split()))

import sys
n = sys.stdin.readline().rstrip()

nList = list(map(int, sys.stdin.readline().rstrip().split()))

m = sys.stdin.readline().rstrip()

mList = list(map(int, sys.stdin.readline().rstrip().split()))


def binarySearch(list, num):
    list.sort()
    start = 0
    end = len(list) - 1
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == num:
            return mid
        elif list[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return False


for i in mList:
    search = binarySearch(nList, i)
    if not search:
        print('0')
    else:
        print('1')

#
# from sys import stdin, stdout
# n = stdin.readline()
# N = sorted(map(int,stdin.readline().split()))
# m = stdin.readline()
# M = map(int, stdin.readline().split())
#
# def binary(l, N, start, end):
#     if start > end:
#         return 0
#     m = (start+end)//2
#     if l == N[m]:
#         return 1
#     elif l < N[m]:
#         return binary(l, N, start, m-1)
#     else:
#         return binary(l, N, m+1, end)
#
# for l in M:
#     start = 0
#     end = len(N)-1
#     print(binary(l,N,start,end))