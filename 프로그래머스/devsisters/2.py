from datetime import datetime, timedelta


def date_range(start, end):
    start = datetime.strptime(start, "%Y/%m/%d")
    end = datetime.strptime(end, "%Y/%m/%d")
    dates = [(start + timedelta(days=i)).strftime("%Y/%m/%d") for i in range((end - start).days + 1)]
    return dates


def solution(join_date, resign_date, holidays):
    answer = 0
    split = join_date.split(' ')

    startDate = split[0]
    date = split[1]

    between_date = date_range(startDate, resign_date)
    print(between_date)

    date_list = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    for i in between_date:
        date_split = i.split('/')
        year = date_split[0]
        month = date_split[1]
        day = date_split[2]

        month_day = month + '/' + day
        print("month_day", month_day)
        if month_day in holidays:
            continue

        today = datetime(int(year), int(month), int(day))
        if 0 <= today.weekday() <= 4:
            print(i)
            answer += 1
            print("answer", answer)

    return answer


# print(solution("2019/12/01 SUN", "2019/12/31", ["12/25"]))
print(solution("2019/12/01 SUN", "2020/03/02", ["01/02", "12/24", "03/01"]))
# print(solution("2019/11/21 THU", "2019/11/21", ["12/23"]))
