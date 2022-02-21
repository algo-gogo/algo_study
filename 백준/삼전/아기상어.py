from collections import deque

# 3
# 0 0 0
# 0 0 0
# 0 9 0

n = int(input())
graph = []

# 상 좌 하 우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    l = list(map(int, input().split()))
    graph.append(l)

sharkX, sharkY = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            sharkX = i
            sharkY = j

print(sharkX, sharkY)
print(graph)

visited = [[False] * n for _ in range(n)]


def bfs(x, y):
    babyShark = 2
    fish = 0
    timeList = []
    queue = deque()
    queue.append((x, y, 0))
    while queue:
        x, y, time = queue.popleft()
        timeList.append(time)
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                visited[nx][ny] = True
                if 0 < graph[nx][ny] < babyShark:
                    fish += 1
                    queue.append((nx, ny, time + 1))
                    if fish == babyShark:
                        babyShark += 1
                elif 0 < graph[nx][ny] == babyShark:
                    queue.append((nx, ny, time))
                else:
                    queue.append((nx, ny, time))

    return max(timeList)


print(bfs(sharkX, sharkY))
