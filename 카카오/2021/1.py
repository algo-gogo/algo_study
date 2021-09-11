# 신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다. 무지가 개발하려는 시스템은 다음과 같습니다.
#
# 각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
# 신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
# 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
# k번 이상 신고된 유저는 즉시 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
# 게시판 이용이 정지된 유저도 불량 이용자를 신고할 수 있습니다.
# 다음은 전체 유저 목록이 ["muzi", "frodo", "apeach", "neo"]이고, k = 2(즉, 2번 이상 신고당하면 이용 정지)인 경우의 예시입니다.
# 이용자의 ID가 담긴 문자열 배열 id_list, 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report, 정지 기준이 되는 신고 횟수 k가 매개변수로 주어질 때, 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수를 완성해주세요.

def report_split(report):
    list1 = []
    list2 = []
    for i in report:
        split = i.split(' ')
        list1.append(split[0])
        list2.append(split[1])
    return list1, list2

def solution(id_list, report, k):
    count = 0
    countList = [ 0 for i in range(len(id_list))]
    answer = [ 0 for i in range(len(id_list))]
    list1 = report_split(report)[0]
    list2 = report_split(report)[1]
    for i in list2:
        for j in range(len(id_list)):
            if i == id_list[j]:
                countList[j] += 1

    for i in range(len(countList)):
        if countList[i] >= k:
            for j in range(len(list2)):
                if list2[j] == id_list[i]:
                    for k in range(len(id_list)):
                        if id_list[k] == list1[j]:
                            answer[k] += 1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))