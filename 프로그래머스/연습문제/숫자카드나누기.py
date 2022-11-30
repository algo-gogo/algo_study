# arrayA에 적힌 모든 숫자를 나눌 수 있다.
# arrayB에 적힌 모든 숫자를 나눌 수 없다.
# 또는 arrayA에 적힌 모든 숫자를 나눌 수 없고, arrayB에 적힌 모든 숫자를 나눌 수 았다.

# def get_divisor(n):
#     data = []
#     for i in range(1, n // 2 + 1):
#         if n % i == 0:
#             data.append(i)
#     data.append(n)
#     return data
#
#
# # 중복값 찾기
# def same_value(a_list):
#     x = []  # 처음 등장한 값인지 판별하는 리스트
#     new_a = []  # 중복된 원소만 넣는 리스트
#
#     for i in a_list:
#         if i not in x:  # 처음 등장한 원소
#             x.append(i)
#         else:
#             if i not in new_a:  # 이미 중복 원소로 판정된 경우는 제외
#                 new_a.append(i)
#
#     return new_a
#
#
# def solution(arrayA, arrayB):
#     a_list = []
#
#     for a in arrayA:
#         divisor = get_divisor(a)
#         a_list += divisor
#
#     b_list = []
#     for b in arrayB:
#         divisor = get_divisor(b)
#         b_list += divisor
#
#     a_same_divisor = same_value(a_list)
#     b_same_divisor = same_value(b_list)
#
#     a_same_divisor.remove(1)
#     b_same_divisor.remove(1)
#     print(a_same_divisor)
#     print(b_same_divisor)
#
#     result_list = []
#     for a in a_same_divisor:
#         flag = False
#         for b in arrayB:
#             if b % a == 0:
#                 flag = True
#                 break
#         if not flag:
#             result_list.append(a)
#
#     for b in b_same_divisor:
#         flag = False
#         for a in arrayA:
#             if a % b == 0:
#                 flag = True
#                 break
#         if not flag:
#             result_list.append(b)
#
#     print(result_list)
#
#     if len(result_list) == 0:
#         return 0
#     return max(result_list)
#
#
# print(solution([10, 17], [5, 20]))
# print(solution([10, 20], [5, 17]))
# print(solution([14, 35, 119], [18, 30, 102]))

def get_divisor(n):
    data = set()
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            data.add(i)
            data.add(n // i)
    data.add(n)
    return sorted(data)

from collections import Counter

def solution(arrayA, arrayB):
    A_lst, B_lst, A_final_lst, B_final_lst, final_lst = [], [], [], [], []

    for i in arrayA:
        A_lst.extend(get_divisor(i))
    for i, j in Counter(A_lst).most_common():
        if j == len(arrayA):
            A_final_lst.append(i)

    print(A_final_lst)
    if len(A_final_lst):
        for i in A_final_lst:
            A_flag = 1
            for j in arrayB:
                if j % i != 0:
                    A_flag = 2
            if A_flag != 2 or A_flag != 1:
                final_lst.append(i)

    for i in arrayB:
        B_lst.extend(get_divisor(i))
    for i, j in Counter(B_lst).most_common():
        if j == len(arrayB):
            B_final_lst.append(i)
    if len(B_final_lst):
        for i in B_final_lst:
            B_flag = 1
            for j in arrayA:
                if j % i != 0:
                    B_flag = 2
            if B_flag != 2 or B_flag != 1:
                final_lst.append(i)

    print(final_lst)
    return 0

print(solution([10, 17], [5, 20]))
# print(solution([10, 20], [5, 17]))
# print(solution([14, 35, 119], [18, 30, 102]))