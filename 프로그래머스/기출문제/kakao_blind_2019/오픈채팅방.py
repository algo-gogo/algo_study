# def solution(record):
#     answer = []
#
#     answer_dict = {}
#     for r in record:
#         r = r.split(' ')
#         if r[0] == "Enter":
#             for i in range(len(answer)):
#                 try:
#                     user_id = answer_dict[r[1]]
#                     if r[1] + user_id in answer[i]:
#                         a = answer[i].replace(answer_dict[r[1]], r[2])
#                         answer[i] = a
#                 except:
#                     pass
#             answer_dict[r[1]] = r[2]
#             answer.append(f"{r[1]}{r[2]}님이 들어왔습니다.")
#         elif r[0] == "Leave":
#             answer.append(f"{r[1]}{answer_dict[r[1]]}님이 나갔습니다.")
#         elif r[0] == "Change":
#             for i in range(len(answer)):
#                 if r[1] + answer_dict[r[1]] in answer[i]:
#                     answer[i] = answer[i].replace(answer_dict[r[1]], r[2])
#             answer_dict[r[1]] = r[2]
#         else:
#             pass
#
#     print(answer_dict)
#     print(answer)
#
#     for i in range(len(answer)):
#         for key, value in answer_dict.items():
#             if key + value in answer[i]:
#                 answer[i] = answer[i].replace(key + value, value)
#
#
#     return answer

def solution(record):
    answer = []

    answer_dict = {}
    for r in record:
        split = r.split(' ')
        if len(split) == 3:
            answer_dict[split[1]] = split[2]

    for i in range(len(record)):
        split = record[i].split(' ')


    print(answer_dict)
    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
