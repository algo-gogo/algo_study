# https://programmers.co.kr/learn/courses/30/lessons/60063

from collections import deque

# def turn

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(array):
    queue = deque()
    queue.append(((0, 0), (0, 1), 0))
    result = 0
    while queue:
        qmatrix1, qmatrix2, count = queue.popleft()
        result = count
        for i in range(4):
            nx1 = qmatrix1[0] + dx[i]
            ny1 = qmatrix1[1] + dy[i]
            nx2 = qmatrix2[0] + dx[i]
            ny2 = qmatrix2[1] + dy[i]
            if 0 <= nx1 < len(array) and 0 <= ny1 < len(array) and 0 <= nx2 < len(array) and 0 <= ny2 < len(array):
                if array[nx1][ny1] == 0 and array[nx2][ny2] == 0:
                    queue.append(((nx1, ny1), (nx2, ny2), count + 1))
            else:
                continue

    return result

    ### 이거 회전을 언제해야하나??


def solution(board):
    # 좌표와 카운트
    return bfs(board)



solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]])
