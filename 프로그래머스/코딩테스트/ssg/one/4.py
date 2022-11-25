from itertools import combinations


def check_right_list(left_sum, right_list):
    try:
        right_sum_list = []
        for i in range(1, len(right_list)):
            for c in list(combinations(right_list, i)):
                if sum(list(c)) == left_sum:
                    right_sum_list.append(i)

        return max(right_sum_list)
    except:
        return 0


def left_right(combi, weights):
    left_length = len(combi)
    left_list = []
    right_list = []

    for index, value in enumerate(weights):
        if index in combi:
            left_list.append(weights[index])
        else:
            right_list.append(weights[index])

    print(left_list)
    print(right_list)

    # 길이가 1이거나
    if (len(left_list) == 1 or sum(left_list) % 2 == 0) and (len(right_list) == 1 or sum(right_list) % 2 == 0):
        return check_right_list(sum(left_list), right_list) + left_length
    else:
        return 0


def solution(weights):
    if len(weights) == 1:
        return 1
    else:
        result_sum_list = []
        length = len(weights)
        w_list = [i for i in range(length)]

        for i in range(1, length):
            combi_list = list(combinations(w_list, i))
            print(combi_list)
            for combi in combi_list:
                result_sum_list.append(left_right(combi, weights))

        print(result_sum_list)
        print(max(result_sum_list))

print(solution([2, 2, 2, 2, 3, 3, 5, 6]))
# print(solution([3, 3, 3, 3, 3, 3, 12]))
# print(solution([16, 16, 16, 16, 16, 16, 16, 16, 1, 1, 2, 4, 4]))
# print([1])
