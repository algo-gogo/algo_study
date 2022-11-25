# https://programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations

def solution(orders, course):
    answer = []

    food_combination = {}

    for order in orders:
        for c in course:
            order_combi = list(combinations(order, c))
            for oc in order_combi:
                oc = tuple(sorted(oc))
                try:
                    food_combination[oc] += 1
                except:
                    food_combination[oc] = 1

    sorted_dict = sorted(food_combination.items(), key=lambda item: item[1], reverse=True)
    print(sorted_dict)
    print(food_combination)

    result_dic = {}

    for sd in sorted_dict:
        if sd[1] > 1:
            # try:
            #     result_dic[len(sd[0])]
            # except:
            #     pass
            if len(sd[0]) not in result_dic:
                result_dic[len(sd[0])] = [sd[1], sd[0]]
            else:
                if result_dic[len(sd[0])][0] == sd[1]:
                    result_dic[len(sd[0])].append(sd[0])

    print(result_dic)
    result_list = []
    for key, value in result_dic.items():
        for i in range(len(value) - 1):
            join = ''.join(list(value[i + 1]))
            result_list.append(join)


    result_list.sort()
    print(result_list)

    return result_list


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
