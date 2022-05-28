import math
from itertools import combinations


def solution(fuel, powers, distances):
    fuel_list_combi = list(combinations(range(1, fuel), len(powers)))

    answer_list = []
    for fuel in fuel_list_combi:
        result_list = []
        fuel_list = list(fuel)
        for i in range(len(powers)):
            increment_length = fuel_list[i] * (powers[i] * fuel_list[i]) // 2
            distance = (distances[i] - increment_length) / (fuel_list[i] * powers[i])
            result = distance + fuel_list[i]
            ceil_result = math.ceil(result)
            result_list.append(ceil_result)

        answer_list.append(max(result_list))

    print(answer_list)

    if len(answer_list) == 0:
        return 0
    return min(answer_list)


# print(solution(8, [20, 30], [750, 675]))
print(solution(19, [40, 30, 20, 10], [1000, 2000, 3000, 4000]))
# print(solution(100, [100, 150], [1, 1000000]))
# print(solution(5, [1, 2, 3, 4, 5], [50, 40, 30, 20, 10]))
