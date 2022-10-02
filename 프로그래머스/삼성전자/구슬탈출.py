# https://www.acmicpc.net/problem/13460
#         5 5
#         #####
#         #..B#
#         #.#.#
#         #RO.#
#         #####

# . 빈칸
# # 장애물
# 0 구멍
# R 빨간 구슬
# B 파란 구슬

from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    l = list(input().rstrip())
    graph.append(l)

print(graph)
print(graph[0][0])

blue_x = 0
blue_y = 0
red_x = 0
red_y = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'B':
            blue_x = i
            blue_y = j
        if graph[i][j] == 'R':
            red_x = i
            red_y = j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 2000주를 가지고 있다면? -> 1,000,000
queue = deque()
queue.append(((blue_x, blue_y), (red_x, red_y), 0))

#
while queue:
    blue, red, count = queue.popleft()
    print(blue)
    print(red)
    print(count)
    for i in range(4):
        bx = blue[0] + dx[i]
        by = blue[1] + dy[i]
        rx = red[0] + dx[i]
        ry = red[1] + dy[i]

