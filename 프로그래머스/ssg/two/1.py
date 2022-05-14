# def solution(v, a, b):
#     # 차가 한대인 경우
#     if len(v) == 1:
#         return v[0] // a
#
#     # 연료 사용량이 동일한 경우
#     if a == b:
#         return min(v) // a
#
#     v.sort()
#
#     time = 0
#     while v[0] // b > 0 and v[-1] // a > 0:
#         max_value = v[-1]
#         max_second_value = v[-2]
#         min_value = v[0]
#
#         gap = max_value - max_second_value
#
#         lead_time = min(max(gap // (a - b), 1), min_value // b, max_value // a)
#
#         if lead_time > 0:
#             for i in range(len(v) - 1):
#                 v[i] -= lead_time * b
#
#             v[-1] -= lead_time * a
#
#         # 선두 교체
#         v[-1], v[-2] = v[-2], v[-1]
#
#         time += lead_time
#
#     return time

def solution(v,a,b):
    # 차가 한대인 경우
    if len(v) == 1:
        return v[0] // a

    # 연료 사용량이 동일한 경우
    if a == b:
        return min(v) // a

    time = 0
    while min(v) // b > 0 and max(v) // a > 0:

        max_idx = v.index(max(v))
        new_v = v.copy()
        new_v.pop(max_idx)
        max_value = max(v)
        max_second_value = max(new_v)
        min_value = min(v)

        gap = max_value - max_second_value

        lead_time = min(max(gap//(a-b), 1), min_value//b, max_value//a)

        if lead_time > 0:
            for i in range(len(v)):
                if i == max_idx:
                    continue
                v[i] -= lead_time * b

            v[max_idx] -= lead_time * a

        time += lead_time

    return time


print(solution([4, 5, 5], 2, 1))
print(solution([4, 4, 3], 2, 1))
