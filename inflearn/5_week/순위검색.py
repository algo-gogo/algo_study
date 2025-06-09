# 다시풀기

# def solution(info, query):
#     answer = [0] * len(query)
#     print(answer)
#
#     for i in range(len(query)):
#         query_list = query[i].replace("and", " ").split()
#         print("query_list", query_list)
#         for j in range(len(info)):
#             info_list = info[j].split()
#             print("info_list", info_list)
#             if ((info_list[0] in query_list[0] or query_list[0] == "-")
#                     and (info_list[1] in query_list[1] or query_list[1] == "-")
#                     and (info_list[2] in query_list[2] or query_list[2] == "-")
#                     and (info_list[3] in query_list[3] or query_list[3] == "-")):
#                 if int(info_list[4]) >= int(query_list[4]):
#                     answer[i] += 1
#
#     return answer

def solution(info, query):
    answer = [0] * len(query)
    print(answer)

    info_dict = {}
    for i in range(len(info)):
        info_list = info[i].split()
        print("info_list", info_list)
        if info_list[0] not in info_dict:
            info_dict[info_list[0]] = [i]
        else:
            info_dict[info_list[0]].append(i)
        if info_list[1] not in info_dict:
            info_dict[info_list[1]] = [i]
        else:
            info_dict[info_list[1]].append(i)
        if info_list[2] not in info_dict:
            info_dict[info_list[2]] = [i]
        else:
            info_dict[info_list[2]].append(i)
        if info_list[3] not in info_dict:
            info_dict[info_list[3]] = [i]
        else:
            info_dict[info_list[3]].append(i)

    print(info_dict)

    for i in range(len(query)):
        query_list = query[i].replace("and", " ").split()
        print("query_list", query_list)
        all_count = query_list.count("-")
        count_list = []
        if query_list[0] != '-' and query_list[0] in info_dict:
            count_list.append(info_dict[query_list[0]])
        if query_list[1] != '-' and query_list[1] in info_dict:
            count_list.append(info_dict[query_list[1]])
        if query_list[2] != '-' and query_list[2] in info_dict:
            count_list.append(info_dict[query_list[2]])
        if query_list[3] != '-' and query_list[3] in info_dict:
            count_list.append(info_dict[query_list[3]])

        print(count_list)
        flattened = sum(count_list, [])
        print(flattened)


    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
               , ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))