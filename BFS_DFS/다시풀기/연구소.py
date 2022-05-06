################################# 연구소
# https://www.acmicpc.net/problem/14502

from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
graph = []

for i in range(n):
    l = list(map(int, input().split()))
    graph.append(l)

zero_list = []
virus_list = []
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero_list.append((i, j))
        if graph[i][j] == 2:
            virus_list.append((i, j))

wall = 3

combi_list = list(combinations(zero_list, wall))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_safe(graph):
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1

    return count

def bfs(graph, virus_list, visited):
    for vx, vy in virus_list:
        queue = deque()
        queue.append((vx, vy))

        while queue:
            vx, vy = queue.popleft()
            for i in range(4):
                nx = vx + dx[i]
                ny = vy + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and graph[nx][ny] == 0:
                        graph[nx][ny] = 2
                        queue.append((nx, ny))

    return find_safe(graph)


result_list = []
for combi in combi_list:
    copy_graph = copy.deepcopy(graph)
    copy_visited = copy.deepcopy(visited)
    for cx, cy in combi:
        copy_graph[cx][cy] = 1
    result_list.append(bfs(copy_graph, virus_list, copy_visited))

print(max(result_list))