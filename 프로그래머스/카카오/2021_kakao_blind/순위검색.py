# https://programmers.co.kr/learn/courses/30/lessons/72412

# def solution(info, query):
#     query_list = []
#     for q in query:
#         print(q)
#         replace = q.replace("and ", "")
#         split = replace.split(" ")
#         query_list.append(split)
#
#     info_list = []
#     for i in info:
#         split = i.split(" ")
#         info_list.append(split)
#
#     print(query_list)
#     print(info_list)
#
#     result_list = []
#     for query in query_list:
#         count = 0
#         for info in info_list:
#             break_point = 0
#             # for q in query:
#             #     if q != '-' and q not in info:
#             #         break_point = -1
#             #         break
#             #     if query[-1] <= info[-1]:
#             #         pass
#             for i in range(len(query) - 1):
#                 if query[i] != '-' and query[i] not in info:
#                     break_point = -1
#                     break
#             if int(query[-1]) > int(info[-1]):
#                 break_point = -1
#             if break_point != -1:
#                 count += 1
#         result_list.append(count)
#
#     return result_list

from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(information, queries):
    answer = []
    dic = defaultdict(list)
    for info in information:
        info = info.split()
        condition = info[:-1]
        score = int(info[-1])
        for i in range(5):
            case = list(combinations([0, 1, 2, 3], i))
            for c in case:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                dic[key].append(score)

    for value in dic.values():
        value.sort()

    for query in queries:
        query = query.replace("and ", "")
        query = query.split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        count = 0
        if target_key in dic:
            target_list = dic[target_key]
            idx = bisect_left(target_list, target_score)
            count = len(target_list) - idx
        answer.append(count)
    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
