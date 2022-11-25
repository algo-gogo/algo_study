# from itertools import permutations
#
# def solution(A,B):
#     answer = 0
#
#     # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
#     print('Hello Python')
#     a = []
#     for i in A:
#         b = []
#         for j in B:
#             b.append(i * j)
#         a.append(b)
#
#     print(a)
#     p_list = list(permutations([i for i in range(len(A))], len(A)))
#     print(p_list)
#     result_list = []
#     for p in p_list:
#         sum = 0
#         for i in range(len(a)):
#             sum += a[i][p[i]]
#         result_list.append(sum)
#
#     return min(result_list)
#
# print(solution([1, 4, 2], [5, 4, 4]))
# # print(solution([1, 2], [3, 4]))

from itertools import permutations

def solution(A,B):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    a = []
    for i in A:
        b = []
        for j in B:
            b.append(i * j)
        a.append(b)

    print(a)

    return answer

print(solution([1, 4, 2], [5, 4, 4]))
# print(solution([1, 2], [3, 4]))