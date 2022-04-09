from itertools import combinations


def num_plus(copy_list):
    join_list = ''.join(copy_list)
    print(join_list)

    return eval(join_list) % (10 ** 9 + 7)


def solution(num, k):
    num_list = []
    index_list = []
    for index, value in enumerate(num):
        num_list.append(value)
        index_list.append(index)

    index_list.pop(-1)
    print(num_list)
    print(index_list)

    combi_list = list(set(combinations(index_list, k)))
    print(combi_list)

    result_list = []
    for i in range(len(combi_list)):
        copy_num_list = num_list[:]
        num = combi_list[i]
        for j in range(len(num)):
            index = num[j] + j
            copy_num_list.insert(index + 1, '+')
        result_list.append(num_plus(copy_num_list))

    print(result_list)

    return min(result_list)


# print(solution("1234567", 2))
# print(solution("555555", 2))
print(solution("91911919", 3))
