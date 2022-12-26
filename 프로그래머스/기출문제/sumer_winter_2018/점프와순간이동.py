# from collections import deque
#
# def my_sort(queue):
#     return deque(sorted(queue, key=lambda x: (x[0], -x[1])))
#
# def bfs(n):
#     queue = deque()
#     queue.append((0, 0))
#     while queue:
#         queue = deque(sorted(queue))
#         num, count = queue.popleft()
#         if num == n:
#             return count
#         queue.append((num + 1, count + 1))
#         if num != 0:
#             queue.append((num * 2, count))


def solution(n):
    answer = 0

    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
            answer += 1

    return answer

print(solution(5))
print(solution(6))
print(solution(5000))