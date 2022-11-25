from collections import deque


def solution(grid, k):

    n = len(grid)
    m = len(grid[0])

    queue = deque()
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # x, y, k, 야영
    queue.append((0, 0, k, 0))

    while queue:
        x, y, k, result = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                queue.append((nx, ny, k - 1, 0))


    pass


print(solution(["..FF", "###F", "###."], 4))
# print(solution(["..FF", "###F", "###."], 4))
# print(solution(
#     [".F.FFFFF.F", ".########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.", ".#...####F", "...#......"],
#     5))
