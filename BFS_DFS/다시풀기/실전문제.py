########################### 음료수 얼려 먹기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(graph, x, y, n, m):
    if 0 <= x < n and 0 <= y < m:
        if graph[x][y] == 0:
            graph[x][y] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(graph, nx, ny, n, m)
            return True
        else:
            return False


n, m = map(int, input().split())
graph = []
for i in range(n):
    l = list(map(int, input()))
    graph.append(l)

print(graph)

count = 0
for i in range(n):
    for j in range(m):
        if dfs(graph, i, j, n, m):
            count += 1

print(count)

############################ 미로 탈출
