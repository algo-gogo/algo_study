def calculate_plus_10_time(time):
    hour = time // 100
    minute = time % 100
    if minute + 10 > 59:
        hour += 1
        minute = minute + 10 - 60
    else:
        minute += 10
    return hour * 100 + minute

def solution(schedules, timelogs, startday):
    answer = 0

    # 1 -> 5, 6
    # 2 -> 4, 5
    # 3 -> 3, 4
    # 4 -> 2, 3
    # 5 -> 1, 2
    # 6 -> 0, 1
    # 7 -> -1, 0
    for timelog in timelogs:
        timelog[7 - startday] = 0
        timelog[7 - startday - 1] = 0
    print(timelogs)
    print(schedules)

    for i in range(len(timelogs)):
        time = calculate_plus_10_time(schedules[i])
        flag = True
        for j in range(len(timelogs[i])):
            if timelogs[i][j] == 0:
                pass
            else:
                if timelogs[i][j] > time:
                    flag = False
        if flag:
            answer += 1

    return answer

print(solution([700, 800, 1100],
               [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]]
               , 5))

print(solution([730, 855, 700, 720],
               [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]],
               1))