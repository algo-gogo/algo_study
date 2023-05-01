from collections import deque


def solution(M, S, D):
    answer = 0
    n, m = len(M), len(M[0])

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    queue = deque()
    queue.append((S[1], S[0], 0))

    num_paths = {(S[1], S[0]): 1}
    min_distance = {(S[1], S[0]): 0}

    while queue:
        x, y, distance = queue.popleft()

        if (x, y) == (D[1], D[0]):
            return num_paths[(x, y)]

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and M[nx][ny] == 0:
                if (nx, ny) not in num_paths:
                    num_paths[(nx, ny)] = num_paths[(x, y)]
                    min_distance[(nx, ny)] = distance + 1
                    queue.append((nx, ny, distance + 1))
                elif min_distance[(nx, ny)] == distance + 1:
                    num_paths[(nx, ny)] += num_paths[(x, y)]

    return num_paths[D[1], D[0]]

print(solution([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [0, 0], [2, 2]))
# print(solution([[0, 0, 1, 0, 0, 0, 0, 0],[0, 0, 0, 1, 0, 1, 0, 0],[0, 0, 0, 1, 0, 1, 0, 0], [0, 1, 1, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
#                , [0, 0], [6, 3]))
