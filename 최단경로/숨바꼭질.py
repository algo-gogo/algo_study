# https://www.acmicpc.net/problem/1697
# 메모리 초과

from collections import deque

d = [-1, 1, 2]

def bfs(n, k):
    queue = deque()
    queue.append((n, 0))
    while queue:
        n, count = queue.popleft()
        if n == k:
            return count
        for i in range(3):
            if i == 2:
                nx = n * 2
            else:
                nx = n + d[i]

            if 0 <= nx:
                queue.append((nx, count + 1))


INF = int(1e9)
n, k = map(int, input().split())

print(bfs(n, k))



