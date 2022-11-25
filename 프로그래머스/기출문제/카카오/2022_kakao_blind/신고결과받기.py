def solution(id_list, report, k):
    answer = []

    print(id_list)
    print(report)

    # id_list 순서대로 신고한 사람 인덱스
    report_list = [[] for _ in range(len(id_list))]

    # id_list 순서대로 신고당한 수
    report_num_list = [0 for _ in range(len(id_list))]

    for index, value in enumerate(list(set(report))):
        split = value.split(' ')
        # 신고한 사람
        a = split[0]
        # 신고 당한사람
        b = split[1]
        for id in id_list:
            if a == id:
                id_index = id_list.index(id)
                report_list[id_index].append(id_list.index(b))


        for id in id_list:
            if b == id:
                id_index = id_list.index(id)
                report_num_list[id_index] += 1

    for index, value in enumerate(report_list):
        report_list[index] = list(set(value))

    print("report_list", report_list)
    print("report_num_list", report_num_list)

    # 신고할 사람 리스트
    answer_list = []
    for index, value in enumerate(report_num_list):
        if value >= k:
            answer_list.append(index)
    print(answer_list)

    result_list = []
    for index, value in enumerate(report_list):
        count = 0
        for i in value:
            if i in answer_list:
                count += 1

        result_list.append(count)

    print(result_list)

    return result_list


print(solution(["muzi", "frodo", "apeach", "neo"],
               ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
               2))

# print(solution(["con", "ryan"],
#                ["ryan con", "ryan con", "ryan con", "ryan con"],
#                3))

# print(solution(["a", "b", "c"], ["a b", "a b", "b c", "c b", "a c"], 2))
