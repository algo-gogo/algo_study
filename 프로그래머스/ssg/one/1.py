from itertools import permutations

def solution(dice):
    n = len(dice)

    graph = [0 for i in range(10 ** n)]

    # 1자리 수
    for index, value in enumerate(dice):
        for v in value:
            graph[v] = 1

    dice_index_list = [0, 1, 2, 3, 4, 5]
    plus_tuple = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]

    aa = 2

    # while aa <= n:
    #     per_list = list(permutations(dice_index_list, aa))
    #     per_list.extend(plus_tuple)
    #     print(per_list)
    #     for per in per_list:
    #         # p_length = len(per)
    #         # for i in range(len(dice) - (p_length - 1)):
    #         #     dice[i][per[0]]
    #         one = dice[0][per[0]]
    #         two = dice[1][per[1]]
    #         value = one * 10 + two
    #         print(value)
    #         graph[value] = 1
    #
    #         one = dice[1][per[0]]
    #         two = dice[0][per[1]]
    #         value = one * 10 + two
    #         print(value)
    #         graph[value] = 1
    #     aa += 1

    while aa <= n:
        per_list = list(permutations(dice_index_list, aa))
        per_list.extend(plus_tuple)
        print(per_list)
        for per in per_list:
            p_length = len(per)
            for i in range(len(dice) - (p_length - 1)):
                p_result = 0
                for p in range(p_length):
                    p_result += dice[i][per[p]] * 10 * (p_length - p)

                graph[p_result] = 1

        aa += 1

    print(graph)

    pass


print(solution([[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]]))
# print(solution([[0, 1, 5, 3, 9, 2], [2, 1, 0, 4, 8, 7], [6, 3, 4, 7, 6, 5]]))
