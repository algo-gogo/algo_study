from itertools import combinations

def solution(n, q, ans):
    global flag
    all_codes = list(combinations(range(1, n + 1), 5))
    print(all_codes)

    result = 0
    for code in all_codes:
        flag = False
        for index, q_list in enumerate(q):
            target_count = 0
            for q_index in q_list:
                if q_index in code:
                    target_count += 1
            if target_count == ans[index]:
                flag = True
            else:
                flag = False
                break
        if flag:
            print(code)
            result += 1

    return result


print(solution(10,
               [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]],
               [2, 3, 4, 3, 3]))
print(solution(15, [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]],
               [2, 1, 3, 0, 1]))