############################## 상하좌우

# 상하좌우
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# n = int(input())
#
# d_input = list(map(str, input().split()))
#
# x, y = 1, 1
#
#
# def move(direction):
#     global x, y, n
#     if direction == 'U':
#         nx = x + dx[0]
#         ny = y + dy[0]
#         if 0 < nx <= n and 0 < ny <= n:
#             x = nx
#             y = ny
#     if direction == 'D':
#         nx = x + dx[1]
#         ny = y + dy[1]
#         if 0 < nx <= n and 0 < ny <= n:
#             x = nx
#             y = ny
#     if direction == 'L':
#         nx = x + dx[2]
#         ny = y + dy[2]
#         if 0 < nx <= n and 0 < ny <= n:
#             x = nx
#             y = ny
#     if direction == 'R':
#         nx = x + dx[3]
#         ny = y + dy[3]
#         if 0 < nx <= n and 0 < ny <= n:
#             x = nx
#             y = ny
#
#
# for index, value in enumerate(d_input):
#     move(value)
#
# print(x, y)


############################## 시각

# n = int(input())
#
# count = 0
# for i in range(n + 1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) or '3' in str(j) or '3' in str(k):
#                 count += 1
#
# print(count)


############################## 왕실의 나이트

# row = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#
# dx = [2, -1, 2, 1]
# dy = [1, 2, -1, 2]
#
# w, h = map(str, input())
#
# x = int(row.index(w))
# y = int(h)
#
# count = 0
#
# for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if 0 < nx <= 8 and 0 < ny <= 8:
#         count += 1
#
# print(count)

############################## 게임 개발

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

# 북 서 남 동
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

graph = []

for i in range(n):
    # 0 은 육지
    # 1 은 바다
    l = list(map(int, input().split()))
    graph.append(l)

visited = [[False for _ in range(n)] for _ in range(m)]

print(graph)
print(visited)

visited[x][y] = True

count = 0
direction_num = 0
while True:
    direction = direction + 1
    nx = x + dx[direction % 4]
    ny = y + dy[direction % 4]
    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 0:
        visited[nx][ny] = True
        x = nx
        y = ny
        count += 1
        direction_num = 0
        continue
    else:
        direction_num += 1
    if direction_num == 4:
        nx = x - dx[direction % 4]
        ny = y - dy[direction % 4]
        if graph[nx][ny] == 1:
            x = nx
            y = ny
        else:
            break
        direction_num = 0

print(count)
