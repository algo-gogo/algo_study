# n X n
# 1번부터 k번까지 바이러스 존재
# 상하좌우로 바이러스 전염
# 낮은순부터 퍼져나감

# 입력: n, k
#    : n개의 줄에걸쳐서 바이러스 행렬
#    : S, X, y  -> S초가 지난 후에 (x, y) 에 있는 바이러스 숫자, 존재하지 않는다면 0

# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2

from collections import deque

queue = deque()
n, m = map(int, input().split())

array = []

for i in range(n):
    l = list(map(int, input().split()))
    array.append(l)

s, x, y = map(int, input().split())

print(array)

for i in range(n):
    for j in range(n):
        for k in range(1, m + 1):
            if array[i][j] == k:
                queue.append((i, j, k, 0))


# def spread(x, y, k, time):
#     if 0 <= x + 1 < n and 0 <= y < n:
#         if array[x + 1][y] == 0:
#             array[x + 1][y] = k
#             queue.append((x+1, y, k, time + 1))
#     if 0 <= x - 1 < n and 0 <= y < n:
#         if array[x - 1][y] == 0:
#             array[x - 1][y] = k
#             queue.append((x - 1, y, k, time + 1))
#     if 0 <= x < n and 0 <= y + 1 < n:
#         if array[x][y + 1] == 0:
#             array[x][y + 1] = k
#             queue.append((x, y + 1, k, time + 1))
#     if 0 <= x < n and 0 <= y - 1 < n:
#         if array[x][y - 1] == 0:
#             array[x][y - 1] = k
#             queue.append((x, y - 1, k, time + 1))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def spread(x, y, k, time):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if array[nx][ny] == 0:
                array[nx][ny] = k
                queue.append((nx, ny, k, time + 1))

# for time in range(s):
#     for i in range(n):
#         for j in range(n):
#             for k in range(1, m + 1):
#                 if array[i][j] == k:
#                     spread(i, j, k)


print(queue)
while queue:
    qx, qy, qk, qTime = queue.popleft()
    if s == qTime:
        break
    spread(qx, qy, qk, qTime)


print(array)
print(array[x - 1][y - 1])

##############################################