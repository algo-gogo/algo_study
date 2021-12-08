# https://www.acmicpc.net/problem/16234


from collections import deque

n, l, r = map(int, input().split())

array = []
array2 = [[False] for _ in range(n) for _ in range(n)]
for i in range(n):
    l = list(map(int, input().split()))
    array.append(l)

print(array)
print(array2)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    array2[x][y] = True
    # count = 1
    # peopleCount = array[x][y]
    country = [(x, y, array[x][y])]
    peopleCount = array[x][y]
    while queue:
        qx, qy = queue.popleft()
        for direction in range(4):
            nx = qx + dx[direction]
            ny = qy + dy[direction]
            if 0 <= nx < n and 0 <= ny < n:
                if l <= abs(array[qx][qy] - array[nx][ny]) <= r:
                    queue.append((nx, ny))
                    country.append((nx, ny, array[nx][ny]))
                    array2[nx][ny] = True
            if array2[nx][ny]:
                continue

    for i, j, count in country:
        array[i][j] = count // len(country)

    return True

result = 0
while True:
    # 다시 원상복귀
    visited = [[False] for _ in range(n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)