from collections import deque

n = int(input())
k = int(input())

graph = [[0 for _ in range(n)] for _ in range(n)]

apple_list = []

for i in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1
    apple_list.append([a - 1, b - 1])

l = int(input())
snake_list = []

# L 왼쪽
# D 오른쪽
for i in range(l):
    a, b = map(str, input().split())
    snake_list.append([a, b])

snake_list.sort(key=lambda x: int(x[0]))

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque()
queue.append((0, 0))


def turn_direction(now_d, after_d):
    if after_d == 'L':
        result_d = (now_d + 3) % 4
    else:
        result_d = (now_d + 1) % 4
    return result_d

print(graph)
print(apple_list)
print("snake_list", snake_list)

result = 0
snake_x = 0
snake_y = 0
snake_d = 1
while True:
    result += 1
    nx = snake_x + dx[snake_d]
    ny = snake_y + dy[snake_d]

    if len(snake_list) != 0:
        if result == int(snake_list[0][0]):
            snake_d = turn_direction(snake_d, snake_list[0][1])
            snake_list.pop(0)
    if 0 <= nx < n and 0 <= ny < n:
        # 자기자신한테 부딫힐 경우
        if [nx, ny] in queue:
            break
        # 사과가 있을 경우
        if [nx, ny] in apple_list:
            apple_list.remove([nx, ny])
            queue.append([nx, ny])
        else:
            queue.append([nx, ny])
            queue.popleft()
        snake_x = nx
        snake_y = ny

    # 벽에 부딫힐 경우
    else:
        break

print(result)