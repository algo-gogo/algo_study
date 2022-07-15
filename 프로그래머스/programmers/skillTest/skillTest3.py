### 숫자 게임
# from itertools import permutations

# def compare_A_B(A, B):
#     score = 0
#     for i in range(len(A)):
#         if A[i] < B[i]:
#             score += 1
#     return score
#
# def solution(A, B):
#     combi_list = list(permutations(B, len(B)))
#     result_list = []
#     for combi in combi_list:
#         result_list.append(compare_A_B(A, combi))
#
#     print(result_list)
#
#     return max(result_list)

# def find_B(a, B):
#     for j in range(len(B)):
#         if a < B[j]:
#             del B[j]
#             return True
#     return False
#
# def solution(A, B):
#     A.sort()
#     B.sort()
#     copy_B = B[:]
#
#     result = 0
#     for i in range(len(A)):
#         value = A[i]
#         if find_B(value, copy_B):
#             result += 1
#
#     return result
#
#
# print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
# print(solution([5, 2, 2, 2], [1, 1, 1, 1]))


# 외벽 점검

from itertools import permutations

def solution(n, weak, dist):
    expansion_weak = weak + [i + 12 for i in weak]
    print(expansion_weak)

    dist.sort(reverse=True)

    print(dist)
    min_count = 1e9
    for i in range(len(weak)):
        for d in permutations(dist):
            count = 1
            position = i
            for j in range(1, len(weak)):
                next_position = i + j
                diff = weak[next_position] - weak[position]
                if diff > d[count - 1]:
                    position = next_position
                    count += 1
                    if count > len(dist):
                        break
            if count < len(dist):
                min_count = min(min_count, count)
    if min_count == 1e9:
        return -1
    return min_count


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
# print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
