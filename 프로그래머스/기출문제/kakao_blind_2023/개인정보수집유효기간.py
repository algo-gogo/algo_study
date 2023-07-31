def dateToday(date):
    year, month, day = map(int, date.split("."))
    return (year * 12 * 28) + (month * 28) + day

def monthToday(month):
    return int(month) * 28

def solution(today, terms, privacies):
    answer = []

    t_dict = {}
    for t in terms:
        split = t.split(' ')
        t_dict[split[0]] = int(split[1])

    today_day = dateToday(today)
    for index, value in enumerate(privacies):
        print('------------')
        print('t_dict', t_dict)
        value_split = value.split(' ')
        date = value_split[0]
        expire_month = t_dict[value_split[1]]
        date_today = dateToday(date)
        month_today = monthToday(expire_month)
        print('date_today', date_today)
        print('month_today', month_today)
        dtd =  + date_today + month_today
        print('today', today_day)
        print('dtd', dtd)
        if today_day >= dtd:
            answer.append(index + 1)

    return answer


print(solution('2022.05.19', ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
# print(solution("2020.01.01", ["Z 3", "D 5"],
#                ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))

