# https://www.acmicpc.net/problem/19236

# graph = []
# graph2 = []
#
# for i in range(4):
#     l = list(map(int, input().split()))
#     a = []
#     for j in range(4):
#         i_ = l[j * 2:j * 2 + 2]
#         i_.append(i)
#         i_.append(j)
#         ti = tuple(i_)
#         a.append(ti)
#         graph2.append(i_)
#     graph.append(a)
#
# moveList = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
# print(graph)
# print(graph2)
# count = 0
# count += graph2[0][0]
# graph2[0][0] = 100
#
# graph2.sort()
# print(graph2)
#
#
# def validateTurn45(x, y, direction):
#     nx = x + moveList[direction % 8][0]
#     ny = y + moveList[direction % 8][1]
#     if nx == 0 and ny == 0:
#         return validateTurn45(x, y, direction + 1)
#     elif 0 <= nx < 4 and 0 <= ny < 4:
#         return nx, ny
#     else:
#         return validateTurn45(x, y, direction + 1)
#
#
# for value, direction, x, y in graph2:
#     # 45도 회전해야하는지 체크
#     if value == 100:
#         continue
#     nx, ny = validateTurn45(x, y, direction - 1)
#
#     index1 = 0
#     index2 = 0
#     for index, i in enumerate(graph2):
#         if i[2] == x and i[3] == y:
#             index1 = index
#         if i[2] == nx and i[3] == ny:
#             index2 = index
#
#     graph2[index1][2], graph2[index2][2] = graph2[index2][2], graph2[index1][2]
#     graph2[index1][3], graph2[index2][3] = graph2[index2][3], graph2[index1][3]
#
# print(graph2)
# sharkPosition = graph2[-1]
# sharkDirection = int(sharkPosition[1])
# sharkX = sharkPosition[2]
# sharkY = sharkPosition[3]
#
#
# def findFish(sharkX_, sharkY_):
#     global count
#     for index_, g in enumerate(graph2):
#         sharkNx = sharkX_ + moveList[sharkDirection - 1][0]
#         sharkNy = sharkY_ + moveList[sharkDirection - 1][1]
#         if g[2] == sharkNx and g[3] == sharkNy:
#             count += graph2[index_][0]
#             sharkX_ = sharkNx
#             sharkY_ = sharkNy
#             return findFish(sharkX_, sharkY_)
#         elif 0 <= sharkNx < 4 and 0 <= sharkNy < 4:
#             pass
#         else:
#             break
#     return count
#
#
# print(findFish(sharkX, sharkY))
# print(count)

# for index, i in enumerate(graph2):
#     nx = sharkX + moveList[sharkDirection - 1][0]
#     ny = sharkY + moveList[sharkDirection - 1][1]
#     if i[2] == nx and i[3] == ny:
#         count += graph2[index][0]


# import copy
#
# moveList = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
#
# def eat_fish(array, x, y):
#     position = []
#     direction = array[x][y][1]
#     for i in range(4):
#         nx = x + moveList[direction][0]
#         ny = y + moveList[direction][1]
#         if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= array[nx][ny][0] <= 16:
#             position.append([nx, ny])
#         x, y = nx, ny
#     return position
#
#
# def validateTurn45(x, y, direction, nowX, nowY):
#     nx = x + moveList[direction % 8][0]
#     ny = y + moveList[direction % 8][1]
#     if nx == nowX and ny == nowY:
#         return validateTurn45(x, y, direction + 1, nowX, nowY)
#     elif 0 <= nx < 4 and 0 <= ny < 4:
#         return nx, ny
#     else:
#         return validateTurn45(x, y, direction + 1, nowX, nowY)
#
# def find_fish(array, index):
#     for i in range(4):
#         for j in range(4):
#             if array[i][j][0] == index:
#                 return (i, j)
#
# def move_fish(array, nowX, nowY):
#     for i in range(1, 17):
#         position = find_fish(array, i)
#         if position is None:
#             continue
#         else:
#             x = position[0]
#             y = position[1]
#             direction = array[x][y][0]
#             targetX, targetY = x + moveList[direction][0], y + moveList[direction][1]
#             tx, ty = validateTurn45(targetX, targetY, direction, nowX, nowY)
#             array[x][y][0], array[tx][ty][0] = array[tx][ty][0], array[x][y][0]
#             array[x][y][1], array[tx][ty][1] = array[tx][ty][1], array[x][y][1]
#
#
# def dfs(graph, x, y, total):
#     global answer
#     array = copy.deepcopy(graph)
#
#     number = array[x][y][0]
#     array[x][y][0] = -1
#
#     # 1 ~ 17 모두 이동
#     move_fish(array, x, y)
#
#     result = eat_fish(array, x, y)
#     answer = max(answer, total + number)
#     for next_x, next_y in result:
#         dfs(array, next_x, next_y, total + number)
#
#
# graph = []
# graph2 = []
#
# for i in range(4):
#     l = list(map(int, input().split()))
#     a = []
#     for j in range(4):
#         i_ = l[j * 2:j * 2 + 2]
#         a.append(i_)
#     graph.append(a)
#
# print(graph)
#
# answer = 0
# dfs(graph, 0, 0, 0)
# print(answer)


######################### 다시 풀어보기
import copy

array = []

# 상 부터 반시계방향
moveList = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


def shark_food(array, x, y):
    eat_fish = []
    direction = (array[x][y][1] + 1) % 8
    for i in range(3):
        nx = x + moveList[direction][0]
        ny = y + moveList[direction][1]
        if 0 <= nx < 4 and 0 <= ny < 4:
            eat_fish.append([nx, ny])
            x = nx
            y = ny
        else:
            continue
    return eat_fish


def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return [i, j, array[i][j][1]]
    return False


def move_fish(array, now_x, now_y):
    for i in range(1, 17):
        fish = find_fish(array, i)
        if not fish:ㄷ
            continue
        else:
            for d in range(8):
                x = fish[0]
                y = fish[1]
                direction = fish[2]
                real_direction = (direction + d + 1) % 8
                nx = x + moveList[real_direction][0]
                ny = y + moveList[real_direction][1]
                if 0 <= nx < 4 and 0 <= ny < 4 and array[nx][ny][0] > 0:
                    if not (nx == now_x and ny == now_y):
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break
                else:
                    continue

    return array


def dfs(array, x, y, total):
    global answer
    array = copy.deepcopy(array)

    # 상어가 0,0을 먹음
    number = array[0][0][0]
    array[0][0][0] = -1

    ### 물고기 이동
    move_fish(array, x, y)
    # 물고기가 다 이동하고 난 후의 좌표
    print(array)

    ### 상어가 이동 할 수 있는 후보들
    food = shark_food(array, x, y)
    print(food)

    answer = max(answer, total + number)
    for next_x, next_y in food:
        dfs(array, next_x, next_y, total + number)


for i in range(4):
    l = list(map(int, input().split()))
    a = []
    for j in range(4):
        i_ = l[j * 2:j * 2 + 2]
        a.append(i_)
    array.append(a)

print(array)

answer = 0
dfs(array, 0, 0, 0)
print(answer)
