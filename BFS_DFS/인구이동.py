# https://www.acmicpc.net/problem/16234
import copy
from collections import deque

n, l, r = map(int, input().split())

array = []
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    a = list(map(int, input().split()))
    array.append(a)

print(array)
print(visited)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    country = []
    country.append((x, y))
    countryNum = array[x][y]
    checked = []
    while queue:
        qx, qy = queue.popleft()
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny]:
                    continue
                if l <= abs(array[qx][qy] - array[nx][ny]) <= r:
                    visited[nx][ny] = True
                    checked.append(True)
                    queue.append((nx, ny))
                    country.append((nx, ny))
                    countryNum += array[nx][ny]

    if True in checked:
        pass
    else:
        return False

    for cx, cy in country:
        array[cx][cy] = countryNum // len(country)
    return True

result = 0
while True:
    breakPoint = False
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if bfs(i, j):
                result += 1
            else:
                breakPoint = True
                if breakPoint:
                    break
        if breakPoint:
            break
    if breakPoint:
        break

print(result)