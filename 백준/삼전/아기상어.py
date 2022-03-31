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
# def bfs(x, y):
#     global babyShark
#     global fish
#     resultList = []
#     queue = deque()
#     queue.append((x, y, 0))
#     visited = [[False] * n for _ in range(n)]
#     while queue:
#         x, y, time = queue.popleft()
#         for direction in range(4):
#             nx = x + dx[direction]
#             ny = y + dy[direction]
#             if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 if 0 < graph[nx][ny] < babyShark:
#                     queue.append((nx, ny, time + 1))
#                     resultList.append((time + 1, nx, ny))
#                 else:
#                     queue.append((nx, ny, time + 1))
#
#     if resultList:
#         resultList.sort()
#         return resultList[0]
#     else:
#         return False
#
#
# for i in range(len(fishList)):
#     if fish < babyShark:
#         result = bfs(sharkX, sharkY)
#         if not result:
#             break
#         print("result", result)
#         # 현재 먹은 물고기는 0으로 변경
#         graph[result[1]][result[2]] = 0
#         sharkX = result[1]
#         sharkY = result[2]
#         timeList.append(result[0])
#         fish += 1
#         if fish == babyShark:
#             fish = 0
#             babyShark += 1
#
# print(timeList)
# count = 0
# for i in timeList:
#     count += i
#
# print(count)

############### 다시 풀기


from collections import deque

n = int(input())

# graph = [[0 for _ in range(n)] for _ in range(n)]
graph = []

for i in range(n):
    l = list(map(int, input().split()))
    graph.append(l)

print(graph)

fish_list = []
shark_x, shark_y = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0 and graph[i][j] != 9:
            fish_list.append([graph[i][j], i, j])
        elif graph[i][j] == 9:
            shark_x = i
            shark_y = j
            graph[i][j] = 0

baby_shark = 2
fish = 0

# 상 하 좌 우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    global baby_shark
    global fish
    visited = [[False] * n for _ in range(n)]
    queue = deque()
    queue.append((x, y, 0))
    result_list = []
    while queue:
        x, y, time = queue.popleft()
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                if 0 < graph[nx][ny] < baby_shark:
                    queue.append((nx, ny, time + 1))
                    result_list.append((time + 1, nx, ny))
                elif graph[nx][ny] == baby_shark or graph[nx][ny] == 0:
                    queue.append((nx, ny, time + 1))
                else:
                    continue

    if result_list:
        result_list.sort()
        return result_list[0]
    else:
        return False


time_list = []

for i in range(len(fish_list)):
    if fish < baby_shark:
        result = bfs(shark_x, shark_y)
        if not result:
            break
        print("result", result)
        # 현재 먹은 물고기는 0으로 변경
        graph[result[1]][result[2]] = 0
        shark_x = result[1]
        shark_y = result[2]
        time_list.append(result[0])
        fish += 1
        if fish == baby_shark:
            fish = 0
            baby_shark += 1

print(time_list)
count = 0
for i in time_list:
    count += i

print(count)
