# 문제 요약 처음은 (1,1)  입력받은 방향을 따라가서 최종 목적지의 좌표를 구하라
# x, y 좌표가 1보다 작은거, n 보다 큰것들은 버림

# 행과 열의 크기  5
# n = int(input())
#
# # R R U D D
# directs = list(map(str, input().split()))
#
# # R D L U
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# x, y = 1, 1
#
# move_types = ['R', 'D', 'L', 'U']
#
# for direct in directs:
#     for i in range(len(move_types)):
#         if direct == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     if nx < 1 or nx > n or ny < 1 or ny > n:     # nx < n and nx > 1 and
#         continue
#
#     x, y = nx, ny
#
# print(x, y)

# 1. 요약
# 2. 어떤것이 입력으로 주어지는지
# 3. 출력

# 행 렬 이동할 때 튜플로, dx,dy로 쓰는 것 2가지 있음

# ---------------------------------------------------

# N X N 크기의 정사각형 (1,1)에서 시작
# 입력: N의 크기
#      R R R U D D
# 출력: 도착할 좌표

n = int(input())
directList = list(input().split())

print(directList)

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
moveType = ['U', 'D', 'L', 'R']

startX = 1
startY = 1

for i in directList:
    moveTypeIndex = 0
    ### moveType의 인덱스 구하기
    for j in range(len(moveType)):
        if i == moveType[j]:
            moveTypeIndex = j
            break
    nx = startX + dx[moveTypeIndex]
    ny = startY + dy[moveTypeIndex]
    if 0 < nx < n and 0 < ny < n:
        startX = startX + dx[moveTypeIndex]
        startY = startY + dy[moveTypeIndex]

print(startX, end=' ')
print(startY)



















