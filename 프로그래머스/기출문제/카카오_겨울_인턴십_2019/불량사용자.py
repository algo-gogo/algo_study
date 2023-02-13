# def solution(user_id, banned_id):
#     banned_list = []
#     for i in range(len(banned_id)):
#         answer = 0
#         for u in user_id:
#             if len(banned_id[i]) == len(u):
#                 for j in range(len(banned_id[i])):
#                     if banned_id[i][j] == '*':
#                         continue
#                     elif banned_id[i][j] != u[j]:
#                         break
#                 else:
#                     answer += 1
#         banned_list.append(answer)
#
#     print("banned_list", banned_list)
#
#     return banned_id

import copy

def solution(user_id, banned_id):
    banned_list = []
    for i in range(len(banned_id)):
        for u in range(len(user_id)):
            if len(banned_id[i]) == len(user_id[u]):
                for j in range(len(banned_id[i])):
                    if banned_id[i][j] == '*':
                        continue
                    elif banned_id[i][j] != user_id[u][j]:
                        break
                else:
                    banned_list.append([i, u, user_id[u]])

    print("banned_list", banned_list)

    return banned_id


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
