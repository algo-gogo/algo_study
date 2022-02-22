# https://www.acmicpc.net/problem/16236

# from collections import deque
#
# # 3
# # 0 0 0
# # 0 0 0
# # 0 9 0
#
# n = int(input())
# graph = []
# fishList = []
#
# # 상 좌 하 우
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
#
# for i in range(n):
#     l = list(map(int, input().split()))
#     graph.append(l)
#
# sharkX, sharkY = 0, 0
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 9:
#             sharkX = i
#             sharkY = j
#         if 1 <= graph[i][j] <= 6:
#             fishList.append((graph[i][j], i, j))
#
# print(sharkX, sharkY)
# print(graph)
# fishList.sort()
# print(fishList)
#
# # 상어의 크기
# babyShark = 2
# # 물고기 먹은 개수
# fish = 0
# timeList = []
#
#
# # def bfs(x, y):
# #     global babyShark
# #     global fish
# #     global timeList
# #     queue = deque()
# #     queue.append((x, y, 0))
# #     visited = [[False] * n for _ in range(n)]
# #     while queue:
# #         x, y, time = queue.popleft()
# #         timeList.append(time)
# #         for direction in range(4):
# #             nx = x + dx[direction]
# #             ny = y + dy[direction]
# #             if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
# #                 visited[nx][ny] = True
# #                 if 0 < graph[nx][ny] < babyShark:
# #                     fish += 1
# #                     queue.append((nx, ny, time + 1))
# #                     if fish == babyShark:
# #                         fish = 0
# #                         babyShark += 1
# #                 elif 0 < graph[nx][ny] == babyShark:
# #                     queue.append((nx, ny, time))
# #                 else:
# #                     queue.append((nx, ny, time))
#
#
# def move(x, y, destinationX, destinationY):
#     global babyShark
#     queue = deque()
#     queue.append((x, y, 0))
#     visited = [[False] * n for _ in range(n)]
#     while queue:
#         x, y, time = queue.popleft()
#         if x == destinationX and y == destinationY:
#             return time
#         for direction in range(4):
#             nx = x + dx[direction]
#             ny = y + dy[direction]
#             if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 if graph[nx][ny] <= babyShark:
#                     queue.append((nx, ny, time + 1))
#
#
# for fishSize, fx, fy in fishList:
#     if fishSize < babyShark:
#         result = move(sharkX, sharkY, fx, fy)
#         print(result)
#         timeList.append(result)
#         sharkX = fx
#         sharkY = fy
#         fish += 1
#         if fish == babyShark:
#             fish = 0
#             babyShark += 1
#
# print(timeList)

from collections import deque

# 3
# 0 0 0
# 0 0 0
# 0 9 0

n = int(input())
graph = []
fishList = []

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
        if 1 <= graph[i][j] <= 6:
            fishList.append((graph[i][j], i, j))

print(sharkX, sharkY)
print(graph)
fishList.sort()
print(fishList)

# 상어의 크기
babyShark = 2
# 물고기 먹은 개수
fish = 0
timeList = []

def bfs(x, y):
    global babyShark
    global fish
    resultList = []
    queue = deque()
    queue.append((x, y, 0))
    visited = [[False] * n for _ in range(n)]
    while queue:
        x, y, time = queue.popleft()
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                if 0 < graph[nx][ny] < babyShark:
                    queue.append((nx, ny, time + 1))
                    resultList.append((time + 1, nx, ny))
                else:
                    queue.append((nx, ny, time + 1))

    if resultList:
        resultList.sort()
        return resultList[0]
    else:
        return False


for i in range(len(fishList)):
    if fish < babyShark:
        result = bfs(sharkX, sharkY)
        if not result:
            break
        print("result", result)
        # 현재 먹은 물고기는 0으로 변경
        graph[result[1]][result[2]] = 0
        sharkX = result[1]
        sharkY = result[2]
        timeList.append(result[0])
        fish += 1
        if fish == babyShark:
            fish = 0
            babyShark += 1

print(timeList)
count = 0
for i in timeList:
    count += i

print(count)
