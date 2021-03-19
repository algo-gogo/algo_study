# 행 렬
n, m = map(int, input().split())
# (1, 1) 방향   0 1 2 3 (북 동 남 서)
x, y, direction = map(int, input().split())

array = []

# 1111
# 1001
# 1101
# 1111
for i in range(n):
    array.append(list(map(int, input().split())))

d = [[0] * m for i in range(n)]
d[x][y] = 1

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    if direction == 0:
        direction = 3
    else:
        direction -= 1


count = 1
turn_time = 0        # ....
while True:
    turn_left()
    nx = dx[i] + x
    ny = dy[i] + y
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        count += 1
        d[nx][ny] = 1
        x = nx
        y = ny
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        break

print(count)
