# https://programmers.co.kr/learn/courses/30/lessons/43105

# def solution(triangle):
#     answer = 0
#     d = []
#
#     for i in range(0, len(triangle)):
#         dd = []
#         for j in range(len(triangle[i])):
#             if i == 0:
#                 dd.append(triangle[i][j])
#                 continue
#
#             print(d[i - 1][i - 1 - j] + triangle[i][j])
#             dd.append(d[i-1][i - 1 - j] + triangle[i][j])
#         d.append(dd)
#
#     print(d)
#     return max(d[-1])
#
#
# print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

# def solution(triangle):
#     d = [triangle[-1]]
#     print(d)
#     for i in range(len(triangle) - 1, 0, -1):
#         dd = []
#         for j in range(1, len(triangle[i])):
#             a = triangle[i][j - 1] + triangle[i - 1][j - 1]
#             b = triangle[i][j] + triangle[i - 1][j - 1]
#             dd.append(max(a, b))
#         d.append(dd)
#
#     print(d)
#
#
# print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

# n = 5
# input_lst = [[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]
#
# answer_lst = []
# for i in range(n):
#     if i == 0:
#         answer_lst.append(input_lst[0])
#     else:
#         answer_lst.append([0] * (i+1))
#
# for i in range(n):
#     if i == 0:
#         continue
#     for j in range(i+1):
#         if i == j:
#             answer_lst[i][j] = input_lst[i][j] + answer_lst[i - 1][j - 1]
#         elif j == 0:
#             answer_lst[i][j] = input_lst[i][j] + answer_lst[i - 1][j]
#         elif (j + 1) == i:
#             answer_lst[i][j] = input_lst[i][j] + max(answer_lst[i - 1][j - 1], answer_lst[i - 1][j])
#         else:
#             answer_lst[i][j] = input_lst[i][j] + max(answer_lst[i - 1][j - 1], answer_lst[i - 1][j])
#
# # print(answer_lst)
# answer_lst = sum(answer_lst, [])
# print(max(answer_lst))

def solution(triangle):
    d = [[] for _ in range(len(triangle))]
    d[len(triangle) - 1] = triangle[-1]
    for i in range(len(triangle) - 1, 0, -1):
        dd = []
        for j in range(1, len(triangle[i])):
            a = d[i][j - 1] + triangle[i - 1][j - 1]
            b = d[i][j] + triangle[i - 1][j - 1]
            dd.append(max(a, b))
            d[i - 1].append(max(a, b))
    return d[0][0]


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
