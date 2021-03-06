# 보드의 크기 N 6
# 사과의 개수 K 3
# 사과의 개수 좌표 3 4
#              2 5
#              5 3
# 방향 변환 횟수   3
# X초 뒤에 L(왼쪽) D(오른쪽) 3 D
#                       15 L
#                       17 D

### 전체적인 맵을 그림
### 방향으로 한칸 움직임
### snake를 큐로 만듬
### 만약 사과가 있다면 snake 를 추가
### 만약 사과가 없다면 snake 현재 좌표를 추가하고 popleft()를 통해 처음에 들어온 좌표 없애줌

from collections import deque

n = int(input())
k = int(input())

# 전체적인 맵
array = [[0 for i in range(n)] for j in range(n)]

appleList = []
for i in range(k):
    a = list(map(int, input().split()))
    a[0] = a[0] - 1
    a[1] = a[1] - 1
    # 맵에 사과좌표를 넣음
    array[a[0]][a[1]] = 1
    appleList.append(a)

directList = []
directCount = int(input())
for i in range(directCount):
    a = list(map(str, input().split()))
    directList.append(a)

directList.sort(key=lambda x: int(x[0]))
print("directList", directList)
print("array", array)
# 우 상 좌 하
snake = deque([[0, 0]])
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
startX = 0
startY = 0

result = 0

breakPoint = 0
direct = 0

def directionTurn(direction, rl):
    print("direction", direction)
    print("rl", rl)
    if direction == 0:
        direction = 4
    if rl == 'D':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

### 0, 1, 2
directCountCount = 0
while True:
    print("directCountCount", directCountCount)
    result += 1
    nx = startX + dx[direct]
    ny = startY + dy[direct]

    if directCountCount < directCount:
        if result == int(directList[directCountCount][0]):
            direct = directionTurn(direct, directList[directCountCount][1])
            directCountCount += 1
    if 0 <= nx < n and 0 <= ny < n:
        if [nx, ny] in snake:
            breakPoint = -1
            break
        ### 사과가 있을 경우
        if array[nx][ny] == 1:
            array[nx][ny] = 0
            snake.append([nx, ny])
        ### 사과가 없을 경우
        elif array[nx][ny] == 0:
            snake.append([nx, ny])
            snake.popleft()
            print("snake", snake)
        startX = nx
        startY = ny

        continue
    # 벽에 부딫힐 경우
    else:
        breakPoint = -1
        break
print(result)

# ----------------------------------------------------

# from collections import deque
#
# n = int(input())
# k = int(input())
#
# # 전체적인 맵
# array = [[0 for i in range(n)] for j in range(n)]
#
# appleList = []
# for i in range(k):
#     a = list(map(int, input().split()))
#     a[0] = a[0] - 1
#     a[1] = a[1] - 1
#     # 맵에 사과좌표를 넣음
#     array[a[0]][a[1]] = 1
#     appleList.append(a)
#
# change = {}
# l = int(input())
# for _ in range(l):
#     x, c = input().split()
#     change[int(x)] = c
#
# snake = deque([[0, 0]])
#
# # 북 동 남 서
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
#
# d = 1
# times = 0
# nx, ny = 0, 0
#
# def boundary_check(x, y):
#     if 0 <= x < n and 0 <= y < n:
#         return True
#     else:
#         return False
#
# def change_direction(direction, d):
#     if direction == 'D':
#         d = (d + 1) % 4
#     else:
#         d = (d - 1) % 4
#     return d
#
# while True:
#     times += 1
#     nx += dx[d]
#     ny += dy[d]
#     if times in change.keys():
#         d = change_direction(change[times], d)
#
#     if boundary_check(nx, ny):
#         if [nx, ny] in snake:
#             break
#         if array[nx][ny] == 1:
#             array[nx][ny] = 0
#             snake.append([nx, ny])
#
#         elif array[nx][ny] == 0:
#             snake.append([nx, ny])
#             x, y = snake.popleft()
#     else:
#         break
# print(times)
