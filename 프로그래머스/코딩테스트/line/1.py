def solution(logs):
    answer = 0

    # 각각의 공백 위치
    error = {
        0: "team_name",
        3: "application_name",
        6: "error_level",
        9: "message"
    }

    for log in logs:
        if len(log) > 100 or log[0] == " ":
            answer += 1
            continue

        log_partition = log.split()

        if len(log_partition) > 12:
            answer += 1
            continue

        for i in error.keys():
            try:
                if log_partition[i] != error[i]:
                    answer += 1
            except:
                answer += 1

    return answer


print(solution(["team_name : db application_name : dbtest error_level : info message : test",
                "team_name : test application_name : I DONT CARE error_level : error message : x",
                "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever",
                "team_name : oberervability application_name : LogViewer error_level : error"]))
