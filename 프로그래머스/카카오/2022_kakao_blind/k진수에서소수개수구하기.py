import string
import math

tmp = string.digits + string.ascii_lowercase


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


# def is_prime(value):
#     if value == 1:
#         return False
#     for i in range(2, value):
#         if value % i == 0:
#             return False
#     return True

# 소수 판별 함수
def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


# def is_prime(n):
#     array = [True for i in range(n + 1)]
#     # 에라토스테네스의 체
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if array[i]:
#             j = 2
#             while i * j <= n:
#                 array[i * j] = False
#                 j += 1
#
#     return [i for i in range(2, n + 1) if array[i]]


def solution(n, k):
    number = convert(n, k)
    print(number)
    split = number.split('0')
    answer = 0
    filter_split = []
    for index, value in enumerate(split):
        if value != '':
            filter_split.append(value)

    print(split)
    print(filter_split)

    for index, value in enumerate(filter_split):
        if is_prime(int(value)):
            answer += 1

    return answer


# print(solution(437674, 3))
# print(solution(110011, 10))
print(solution(524287, 2))
