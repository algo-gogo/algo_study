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

# 이거 왜 정렬이 안되는거야 **
directList.sort(key=lambda x: x[0], reverse=True)

# print(array)
# 우 상 좌 하
snake = deque([[0, 0]])
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
startX = 0
startY = 0

result = 0

breakPoint = 0
direct = 0
print(directList)


def directionTurn(direction, rl):
    if direction == 0:
        direction = 4
    if rl == 'D':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


for i in range(directCount):
    for j in range(int(directList[i][0])):
        nx = startX + dx[direct]
        ny = startY + dy[direct]
        result += 1
        # 벽에 부딫히지 않을 경우
        if 0 <= nx < n and 0 <= ny < n:
            # for appleX, appleY in appleList:
            #     if appleX == nx and appleY == ny:
            #         body = 1
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
            startX = nx
            startY = ny

            continue
        # 벽에 부딫힐 경우
        else:
            breakPoint = -1
            break
    # 우 상 좌 하
    # directionTurn(direct, directList[i][1])
    if directList[i][1] == 'D' and direct == 0:
        direct = 3
    elif directList[i][1] == 'L' and direct == 0:
        direct = 1
    elif directList[i][1] == 'D' and direct == 1:
        direct = 0
    elif directList[i][1] == 'L' and direct == 1:
        direct = 2
    elif directList[i][1] == 'D' and direct == 2:
        direct = 1
    elif directList[i][1] == 'L' and direct == 2:
        direct = 3
    elif directList[i][1] == 'D' and direct == 3:
        direct = 2
    elif directList[i][1] == 'L' and direct == 3:
        direct = 0
    if breakPoint == -1:
        break

# ----------------------------------------------------



print(result)