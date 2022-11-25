from datetime import datetime, timedelta
from collections import deque

def date_range(start, end):
    start = datetime.strptime(start, "%Y/%m/%d")
    end = datetime.strptime(end, "%Y/%m/%d")
    dates = [(start + timedelta(days=i)).strftime("%Y/%m/%d") for i in range((end-start).days+1)]
    return dates

def solution(masks, dates):
    answer = 0

    print(masks)

    print(dates)
    date_list = []
    for i in dates:
        if i.find('~') != -1:
            split = i.split('~')
            start_date = split[0]
            end_date = split[1]
            range_list = date_range(start_date, end_date)
            date_list.extend(range_list)
            continue
        date_list.append(i)

    date_list = list(set(date_list))
    date_list.sort()
    print(date_list)



    return answer


print(solution([[3200, 4], [2300, 2], [1100, 1], [4200, 6]],
               ["2022/05/02", "2022/05/01", "2022/05/07", "2022/05/05", "2022/05/08", "2022/05/13~2022/05/15",
                "2022/05/14~2022/05/17", "2022/05/01~2022/05/02", "2022/05/16"]))

# print(solution([[600, 2], [500, 1], [1015, 400]], ["2023/01/01~2023/01/02", "2021/12/31"]))
#
# print(solution([[3651, 365], [10, 1]], ["2025/01/01~2025/12/31"]))
