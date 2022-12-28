# import math
#
#
# def solution(n, stations, w):
#     n_list = [0] * (n + 1)
#     n_list[-1] = 1
#     for s in stations:
#         for i in range(s - w - 1, s + w):
#             if i < 0 or i >= n:
#                 continue
#             n_list[i] = 1
#     print(n_list)
#
#     zero_list = []
#     count = 0
#     for n in n_list:
#         if n == 0:
#             count += 1
#         else:
#             if count == 0:
#                 continue
#             if count != 0:
#                 zero_list.append(count)
#                 count = 0
#
#     print(zero_list)
#     answer = 0
#
#     for z in zero_list:
#         answer += math.ceil(z / (2 * w + 1))
#
#     return answer

from math import ceil


def solution(n, stations, w):
    answer = 0
    W = 2 * w + 1

    start = 1
    for s in stations:
        answer += max(ceil((s - w - start) / W), 0)
        start = s + w + 1

    if n >= start:
        answer += ceil((n - start + 1) / W)

    return answer


print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))
