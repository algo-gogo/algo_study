def solution(queue1, queue2):
    make_num = (sum(queue1) + sum(queue2)) // 2

    limit_count = 0
    count = 0
    while sum(queue1) != make_num:
        if limit_count > len(queue1) * len(queue2):
            return -1
        if sum(queue1) < make_num:
            count += 1
            pop_num = queue2.pop(0)
            queue1.append(pop_num)
        else:
            count += 1
            pop_num = queue1.pop(0)
            queue2.append(pop_num)
        limit_count += 1

    return count


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))
