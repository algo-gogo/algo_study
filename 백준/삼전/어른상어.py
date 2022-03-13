# https://www.acmicpc.net/problem/19237

# def solution(h):
#     s = set(h)
#     l = list(s)
#     print(l)
#     print(h)
#     result = []
#     for i in range(len(l)):
#         height = l[i]
#         numList = []
#         for i in range(h):
#

# def solution(h):
#     resultList = []
#     maxHeight = max(h)
#     result = []
#     # result = [[] for i in range(maxHeight)]
#     for i in range(maxHeight):
#         result.append([i + 1, 0])
#
#     print(result)
#     for index, value in enumerate(h):
#         resultList.append([index + 1, value])
#
#     print(resultList)
#
#     for i in range(len(resultList) - 1):
#         height = resultList[i][1]
#         if resultList[i + 1][1] < height:
#             result[height - 1][1] += 1
#
#     print(result)

from collections import deque

def solution(h):

    maxHeight = max(h)
    result = []
    for i in range(maxHeight):
        result.append([i + 1, 0])
    print(result)
    stack = deque()
    answer = 0

    for i in range(len(h)):
        value = h[i]
        stack.append((i, value))
        print(stack)
        if len(stack) == 1:
            result[value - 1][1] += 1
        elif len(stack) == len(h):
            result[value - 1][1] += 1
        else:
            for j in range(len(stack)):
                stackValue = stack[i - 1][1]
                if stackValue >= value:
                    result[value - 1][1] += 1

    return result

print(solution([3, 2, 1, 1, 3]))

# def solution(N, L):
#     answer = 0
#     aa = []
#     for i in range(N):
#         a = []
#         wh = L[i]
#         x1 = wh[0]
#         y1 = wh[1]
#         x2 = wh[2]
#         y2 = wh[3]
#         maxX = max(x1, x2)
#         maxY = max(y1, y2)
#         minX = min(x1, x2)
#         minY = min(y1, y2)
#         for j in range((maxX - minX) + 1):
#             for k in range((maxY - minY) + 1):
#                 a.append((maxX - j, maxY - k))
#         aa.append(a)
#
#     result = 0
#     resultList = []
#     for i in range(len(aa) - 1):
#         for j in aa[i]:
#             for k in aa[i + 1]:
#                 if j == k:
#                     result += 1
#
#     print(result)
#     print(resultList)
#
#     print(aa[0])
#     print(aa[1])
#     print(aa[2])
#
#     return result // 2
#
#
# print(solution(3, [[5, 7, 6, 6], [3, 9, 5, 4], [8, 2, 7, 6]]))
