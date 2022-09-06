from collections import deque


def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    make_num = (q1_sum + q2_sum) // 2

    count = 0
    while queue1 and queue2:
        print("q1", queue1)
        print("q2", queue2)
        if q1_sum == make_num:
            return count
        if q1_sum < make_num:
            pop_num = queue2.popleft()
            queue1.append(pop_num)
            q1_sum += pop_num
        else:
            pop_num = queue1.popleft()
            q1_sum -= pop_num
        count += 1
    return -1


# print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
# print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))
