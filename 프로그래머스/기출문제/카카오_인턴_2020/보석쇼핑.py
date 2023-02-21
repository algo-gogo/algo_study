from collections import Counter


# def solution(gems):
#     answer = []
#
#     gems_dict = {}
#     for i in range(len(gems)):
#         try:
#             gems_dict[gems[i]].append(i + 1)
#         except:
#             gems_dict[gems[i]] = [i + 1]
#
#     print(gems_dict)
#
#     return answer

# def solution(gems):
#     n = len(gems)
#     gems_set = set(gems)
#     answer = [0, n - 1]
#     start, end = 0, 0
#
#     while 0 <= start < n and 0 <= end < n:
#         if set(gems[start: end + 1]) == gems_set:
#             if (end - start + 1) < (answer[1] - answer[0] + 1):
#                 answer = [start, end]
#             start += 1
#         else:
#             end += 1
#
#     answer[0] += 1
#     answer[1] += 1
#
#     return answer

def solution(gems):
    n = len(gems)
    gems_set_num = len(set(gems))
    answer = [0, n - 1]
    start, end = 0, 0
    gems_dict = {gems[0]: 1}

    while 0 <= start < n and 0 <= end < n:
        if len(gems_dict) >= gems_set_num:
            if (end - start + 1) < (answer[1] - answer[0] + 1):
                answer = [start, end]
            if gems_dict[gems[start]] == 1:
                del gems_dict[gems[start]]
            else:
                gems_dict[gems[start]] -= 1

            start += 1
        else:
            end += 1
            if end == n:
                break
            gems_dict[gems[end]] = gems_dict.get(gems[end], 0) + 1

    answer[0] += 1
    answer[1] += 1

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution(["AA", "AB", "AC", "AA", "AC"]))
# print(solution(["XYZ", "XYZ", "XYZ"]))
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
