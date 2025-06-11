from itertools import combinations

def solution(n, q, ans):
    global com_list
    answer = 0

    result_com_list = list(combinations([i for i in range(1, n + 1)], 5))
    print('result_com_list', result_com_list)

    com_list = []
    for i in range(len(q)):
        combination = combinations(q[i], ans[i])
        com_list.append(list(combination))

    print('com_list', com_list)
    # for result_com in result_com_list:
    #     flag = True
    #     print(result_com)
    #     for com in com_list:
    #         if com in result_com:
    #             pass




    return answer

print(solution(10,
               [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]],
               [2, 3, 4, 3, 3]))
print(solution(15, [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]],
               [2, 1, 3, 0, 1]))