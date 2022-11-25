from datetime import datetime, timedelta
from itertools import combinations

def impossible_check(do_not_disturb):
    combi_list = list(combinations(do_not_disturb, 2))
    for combi in combi_list:
        print(combi)
        split = combi[0].split('~')
        start_date_1 = split[0]
        end_date_1 = split[1]
        if start_date_1 > end_date_1:
            end_date_split = end_date_1.split(':')
            end_date_1 = str(int(end_date_split[0]) + 24) + ":" + end_date_split[1]
            temp_start_date_1 = start_date_1
            temp_start_date_split = temp_start_date_1.split(':')
            temp_start_date_1 = str(int(temp_start_date_split[0]) + 24) + ":" + temp_start_date_split[1]
        else:
            temp_start_date_1 = start_date_1

        split = combi[1].split('~')
        start_date_2 = split[0]
        end_date_2 = split[1]
        if start_date_2 > end_date_2:
            end_date_split = end_date_2.split(':')
            end_date_2 = str(int(end_date_split[0]) + 24) + ":" + end_date_split[1]
            temp_start_date_2 = start_date_2
            temp_start_date_split = temp_start_date_2.split(':')
            temp_start_date_2 = str(int(temp_start_date_split[0]) + 24) + ":" + temp_start_date_split[1]
        else:
            temp_start_date_2 = start_date_2


        if start_date_2 < temp_start_date_1 < end_date_2 and start_date_1 < temp_start_date_2 < end_date_1:
            return True


def solution(noti_time, do_not_disturb):
    answer = ''

    if impossible_check(do_not_disturb):
        return "impossible"

    for time in do_not_disturb:
        noti = datetime.strptime(noti_time, "%H:%M")
        split = time.split("~")

        start_date = datetime.strptime(split[0], "%H:%M")
        end_date = datetime.strptime(split[1], "%H:%M")

        if start_date > end_date:
            end_date = end_date + timedelta(days=1)
        if start_date <= noti <= end_date:
            answer = split[1]
            noti_time = split[1]
        else:
            answer = noti_time

    return answer

# print(solution("23:00", ["22:30~23:40", "23:05~00:45"]))
# print(solution("09:55", ["09:55~13:25", "13:25~14:01"]))
print(solution("00:00", ["11:00~23:00", "23:00~13:00"]))
# print(solution("09:55", ["13:25~14:01", "09:56~13:25", "20:08~20:15"]))
# print(solution("23:59", ["00:00~23:59", "11:35~23:59"]))