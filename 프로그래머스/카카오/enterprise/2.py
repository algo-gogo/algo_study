
# ..........
# ..........
# ..........
# ..H.......
# ..........
# .....R....
# ..........
# ..........
# .....M....
# ..........
from collections import deque

table = []
for i in range(10):
    m = list(map(str, input()))
    table.append(m)


x = 0
y = 0

end_x = 0
end_y = 0
for i in range(10):
    for j in range(10):
        if table[i][j] == 'H':
            x = i
            y = j
            table[i][j] = 0
        if table[i][j] == 'M':
            end_x = i
            end_y = j
            table[i][j] = 0
        if table[i][j] == 'R':
            table[i][j] = -1
        if table[i][j] == '.':
            table[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < 10 and 0 <= ny < 10 and table[nx][ny] != -1:
                if table[nx][ny] == 0:
                    table[nx][ny] = table[x][y] + 1
                    queue.append((nx, ny))
            else:
                continue

    print(table)

    return int(table[end_x][end_y]) - 1

print(bfs(x, y))


print("------------")
print("x", x)
print("y", y)
print("dx", dx)
print("dy", dy)

print(table)