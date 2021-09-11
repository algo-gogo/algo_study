
def records_split(records):
    list = []
    for i in records:
        recordsList = []
        split = i.split(' ')
        recordsList.append(split[0])
        recordsList.append(split[1])
        recordsList.append(split[2])
        list.append(recordsList)
    return list

def setTime(s):
    split = s.split(':')
    time = int(split[0]) * 60 + int(split[1])
    return time

def solution(fees, records):
    origin_time = fees[0]
    origin_price = fees[1]
    slice_time = fees[2]
    slice_price = fees[3]
    records_list = records_split(records)
    list = []
    for i in records_list:
        list.append(i[1])

    setList = set(list)
    car_list = []
    for i in setList:
        car_list2 = []
        for j in records_list:
            if j[1] == i:
                car_list2.append(j)
        car_list.append(car_list2)

    for i in car_list:
        if len(i) % 2 == 0:
            print(i)
            time_list = []
            time = 0
            for j in range(1, len(i) // 2):
                time += setTime(i[-j][0]) - setTime(i[-j-1][0])
            time_list.append(time)
            print(time_list)




    answer = []
    return answer

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])