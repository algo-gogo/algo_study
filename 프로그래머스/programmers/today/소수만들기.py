n_list = list(map(int, input().split()))
print(n_list)


# from itertools import combinations
# import math
#
#
# def is_prime_number(x):
#     for i in range(2, int(math.sqrt(x)) + 1):
#         if x % i == 0:
#             return False
#     return True
#
#
# def solution(nums):
#     answer = 0
#     combi_list = list(combinations(nums, 3))
#
#     for i in combi_list:
#         sum_value = sum(i)
#         if is_prime_number(sum_value):
#             answer += 1
#
#     return answer


