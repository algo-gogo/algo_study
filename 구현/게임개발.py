# 행 열
n, m = map(int, input().split())

# 1, 1, 0          0 - 북, 1 - 동, 2 - 남, 3 - 서
x, y, direct = map(int, input().split())

# array = []
# for i in range(n):
#     array.append(list(map(int, input().split())))
#
# # 방향
# dx = [-1, 0, 1, 0]   # 북 서 남 동
# dy = [0, -1, 0, 1]   # 북 서 남 동
#
# direct_types = [0, 3, 2, 1]
# count = 1
#
#
#
# while True:
#     if direct == direct_types[0]:   # 북
#         nx = x + dx[0]
#         ny = y + dy[0]
#         if array[nx][ny] == 0:
#             count += 1
#             x, y = nx, ny

###################################################

n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]

x, y, direct = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]  # 북 동 남 서
dy = [0, 1, 0, -1]


def turn_left():
    global direct
    direct -= 1
    if direct == -1:
        direct = 3


count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direct]
    ny = y + dy[direct]
    # 회전한 후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direct]
        ny = y - dy[direct]
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
