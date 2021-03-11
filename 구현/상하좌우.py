# 행과 열의 크기  5
n = int(input())

# R R U D D
directs = list(map(str, input().split()))

# R D L U
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 1, 1

move_types = ['R', 'D', 'L', 'U']

for direct in directs:
    for i in range(len(move_types)):
        if direct == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue

    x, y = nx, ny

print(x, y)
