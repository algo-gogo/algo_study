# https://programmers.co.kr/learn/courses/30/lessons/92345

# minMax 알고리즘?

from collections import deque
def bfs():
    pass

def solution(board, aloc, bloc):
    answer = -1
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 0
    queue = deque()
    queue.append((aloc[0], aloc[1], count))
    queue.append((bloc[0], bloc[1], count))
    print(queue)
    while queue:
        popleft = queue.popleft()
        print(popleft)


    return answer


print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))
print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]))
print(solution([[1, 1, 1, 1, 1]], [0, 0], [0, 4]))
print(solution([[1]], [0, 0], [0, 0]))
