# https://www.acmicpc.net/problem/19237

from collections import deque

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m, k = map(int, input().split())

graph = []
for i in range(n):
    l = list(map(int, input().split()))
    graph.append(l)

sharkDirection = list(map(int, input().split()))

# 상 하 좌 우
sharkDirectionNum = []

for i in range(m):
    for j in range(4):
        l = list(map(int, input().split()))
        sharkDirectionNum.append(l)

queue = deque()
# 상어의 위치
shark = []
# 냄새 위치
smell = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            queue.append((i, j, graph[i][j], sharkDirection[graph[i][j] - 1]))
            shark.append([i, j, graph[i][j], sharkDirection[graph[i][j] - 1]])
            # k를 -1 씩 해서 0이되면 pop 시킬 예정
            smell.append([i, j, graph[i][j], k])

print("sharkDirectionNum", sharkDirectionNum)
print("shark", shark)
print("smell", smell)
print(queue)

def move(x, y, shark, direction):
    # 움직이고 smell에 append 하고 기존꺼 k - 1
    # 움직이면서 1번 상어랑 만나면 먹힘...

    # 우선순위 리스트
    priceDirection = sharkDirectionNum[shark * 4 - direction]
    for i in range(4):
        nx = x + dx[priceDirection[i]]
        ny = y + dy[priceDirection[i]]
        if 0 <= nx < n and 0 <= ny < n:
            # 만약 smell에 1번향수 또는 상어가 있으면 먹힘

            # 아닐 경우 queue에 넣고 ....
            queue.append([nx, ny, shark, priceDirection[i]])
            for j in range(len(smell)):
                smell[j][3] = smell[j][3] - 1
                if smell[j][3] == 0:
                    del smell[j]
            smell.append([nx, ny, shark, k])
        break

while queue:
    # x, y, 상어번호, 방향
    x, y, shark, direction = queue.popleft()
    move(x, y, shark, direction)
