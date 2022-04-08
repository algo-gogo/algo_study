def solution(fees, records):
    answer = []

    # 기본 시간, 기본 요금, 단위 시간, 단위 요금
    print(fees)
    print(records)

    car_list = []
    car_check = []
    for index, value in enumerate(records):
        split = value.split(' ')
        car = []
        print(split)
        if split[1] not in car_check:
            car_check.append(split[1])
            car.append(split[1])
            a = [split[0], split[2]]
            car.append(a)
            car_list.append(car)
        else:
            for j, value2 in enumerate(car_list):
                if value2[0] == split[1]:
                    a = [split[0], split[2]]
                    car_list[j].append(a)

    print(car_check)
    print(car_list)

    return answer


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

# print(solution([120, 0, 60, 591],
#                ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
#
# print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
