# 보드의 크기 N 6
# 사과의 개수 K 3
# 사과의 개수 좌표 3 4
#              2 5
#              5 3
# 방향 변환 횟수   3
# X초 뒤에 L(왼쪽) D(오른쪽) 3 D
#                       15 L
#                       17 D

n = int(input())
k = int(input())
appleList = []
for i in range(k):
    a = list(map(int, input().split()))
    a[0] = a[0] - 1
    a[1] = a[1] - 1
    appleList.append(a)

directList = []
directCount = int(input())
for i in range(directCount):
    a = list(map(str, input().split()))
    directList.append(a)

# 이거 왜 정렬이 안되는거야 **
directList.sort(key=lambda x: x[0], reverse=True)

array = [[0 for i in range(n)] for j in range(n)]
# print(array)
# 우 상 좌 하
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
startX = 0
startY = 0

result = 0

breakPoint = 0
direct = 0
print(directList)
for i in range(directCount):
    for j in range(int(directList[i][0])):
        nx = startX + dx[direct]
        ny = startY + dy[direct]
        result += 1
        if 0 <= nx < n and 0 <= ny < n:
            startX = nx
            startY = ny
            continue
        else:
            breakPoint = -1
            break
    # 우 상 좌 하
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


print(result)