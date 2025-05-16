### 슈퍼 로봇 대전
# https://www.acmicpc.net/problem/3665
# 5 5
# 4 3
# 4 2
# 3 2
# 1 2
# 2 5


# n - 로봇의 개수
# m - 라운드

from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[b].append(a)
    indegree[a] += 1

print(indegree)
for i in range(len(graph)):
    indegree[i] += len(graph[i]) - 1


def topology_sort():
    result = []
    queue = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    print(graph)
    print(indegree)
    print(result)

    if len(result) == 0:
        print(v)
    else:
        print(len(result))


topology_sort()
