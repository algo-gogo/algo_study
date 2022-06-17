def solution(p):
    result_list = [0 for _ in range(len(p))]

    for i in range(len(p) - 1):
        value = p[i]
        left_list = p[i + 1:]
        left_list_min_value = min(left_list)
        if value > left_list_min_value:
            left_list_index = left_list.index(left_list_min_value) + i + 1
            p[i], p[left_list_index] = p[left_list_index], p[i]
            result_list[i] += 1
            result_list[left_list_index] += 1

    return result_list

print(solution([2, 5, 3, 1, 4]))
print(solution([2, 3, 4, 5, 6, 1]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))
