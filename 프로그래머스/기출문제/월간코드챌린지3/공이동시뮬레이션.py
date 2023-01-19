def solution(n, m, x, y, queries):
    answer = 0

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    board = [[0] * m for _ in range(n)]
    print(board)

    for i in range(n):
        for j in range(m):
            cx = i
            cy = j
            for q in queries:
                nx = cx + dx[q[0]] * q[1]
                ny = cy + dy[q[0]] * q[1]
                if 0 <= nx < n and 0 <= ny < m:
                    cx = nx
                    cy = ny
            if cx == x and cy == y:
                answer += 1

    return answer


print(solution(2, 2, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]))
print(solution(2, 5, 0, 1, [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]]))
