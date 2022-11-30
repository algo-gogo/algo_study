import math


def solution(record):
    answer = []

    record_dict = {}
    one = []
    two = []
    three = []
    four = []
    five = []
    length = len(record)
    for r in record:
        split = r.split(':')
        name = split[0]
        c = split[1].split(',')
        if int(c[0]) != 0:
            one.append(int(c[0]))
        if int(c[1]) != 0:
            two.append(int(c[1]))
        if int(c[2]) != 0:
            three.append(int(c[2]))
        if int(c[3]) != 0:
            four.append(int(c[3]))
        if int(c[4]) != 0:
            five.append(int(c[4]))

    gold_medal_percent = math.ceil(length / 12) - 1
    silver_medal_percent = math.ceil(length / 4) - 1
    bronze_medal_percent = math.ceil(length / 2) - 1
    one.sort()
    two.sort()
    three.sort()
    four.sort()
    five.sort()
    medal_list = [one, two, three, four, five]

    for r in record:
        split = r.split(':')
        name = split[0]
        c = split[1].split(',')

        # 완주 개수, 가장 어려운 코스, 완주 합
        count = 0
        hard = 1
        c_sum = 0
        gold_medal_count = 0
        silver_medal_count = 0
        bronze_medal_count = 0
        for index, value in enumerate(c):
            if value != '0':
                print("dd", medal_list[index][gold_medal_percent])
                if int(value) <= medal_list[index][gold_medal_percent]:
                    gold_medal_count += 1
                elif int(value) <= medal_list[index][silver_medal_percent]:
                    silver_medal_count += 1
                elif int(value) <= medal_list[index][bronze_medal_percent]:
                    bronze_medal_count += 1
                hard = index + 1
                count += 1
                c_sum += int(value)

        record_dict[name] = [c, count, hard, gold_medal_count, silver_medal_count, bronze_medal_count, c_sum]

    print(record_dict)
    record_dict_sort = sorted(record_dict.items(), key=lambda x: (-x[1][1], x[1][2], -x[1][3], -x[1][4], -x[1][5], -x[1][6]))
    print(record_dict_sort)

    return answer


print(solution(
    ["jack:9,10,13,9,15", "jerry:7,7,14,10,17", "jean:0,0,11,20,0", "alex:21,2,7,11,4", "kevin:8,4,5,0,0",
     "brown:3,5,16,3,18", "ted:0,8,0,0,8", "lala:0,12,0,7,9", "hue:17,16,8,6,10", "elsa:11,13,10,4,13"]))
