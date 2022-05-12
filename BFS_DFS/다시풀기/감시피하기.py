# https://www.acmicpc.net/problem/18428
from itertools import combinations
import copy


n = int(input())
graph = []
for i in range(n):
    l = list(map(str, input().split()))
    graph.append(l)

print(graph)

x_list = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'X':
           x_list.append([i, j])

print(x_list)

combi_list = list(combinations(x_list, 3))
print(combi_list)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, copy_graph):
    # for i in range(4):
    #     nx = x + dx[i]
    #     ny = y + dy[i]
    #     if 0 <= nx < n and 0 <= ny < n:
    #         if copy_graph[nx][ny] == 'O':
    #             continue
    #         if copy_graph[nx][ny] == 'S':
    #             return False
    # return True
    # 상
    # 하
    # 좌
    # 우
    pass
def up(x, y, copy_graph):
    nx = x + dx[0]
    ny = y + dy[0]
    if 0 <= nx < n and 0 <= ny < n:
        if copy_graph[nx][ny] == 'X':
            return up(nx, ny, copy_graph)
        elif copy_graph[nx][ny] == 'S':
            return False
        elif copy_graph[nx][ny] == 'O':
            return True
    return True
def down(x, y, copy_graph):
    nx = x + dx[1]
    ny = y + dy[1]
    if 0 <= nx < n and 0 <= ny < n:
        if copy_graph[nx][ny] == 'X':
            return down(nx, ny, copy_graph)
        if copy_graph[nx][ny] == 'S':
            return False
        if copy_graph[nx][ny] == 'O':
            return True
    return True
def left(x, y, copy_graph):
    nx = x + dx[2]
    ny = y + dy[2]
    if 0 <= nx < n and 0 <= ny < n:
        if copy_graph[nx][ny] == 'X':
            return left(nx, ny, copy_graph)
        if copy_graph[nx][ny] == 'S':
            return False
        if copy_graph[nx][ny] == 'O':
            return True
    return True
def right(x, y, copy_graph):
    nx = x + dx[3]
    ny = y + dy[3]
    if 0 <= nx < n and 0 <= ny < n:
        if copy_graph[nx][ny] == 'X':
            return right(nx, ny, copy_graph)
        if copy_graph[nx][ny] == 'S':
            return False
        if copy_graph[nx][ny] == 'O':
            return True
    return True

def check_teacher(copy_graph):
    print(copy_graph)
    for i in range(n):
        for j in range(n):
            if copy_graph[i][j] == 'T':
                if not up(i, j, copy_graph):
                    return False
                if not down(i, j, copy_graph):
                    return False
                if not left(i, j, copy_graph):
                    return False
                if not right(i, j, copy_graph):
                    return False
    return True

result_list = []
for combi in combi_list:
    copy_graph = copy.deepcopy(graph)
    for c in combi:
        copy_graph[c[0]][c[1]] = 'O'
    result_list.append(check_teacher(copy_graph))

print(result_list)

if True in result_list:
    print('YES')
else:
    print('NO')