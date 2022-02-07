# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

from collections import deque
from copy import deepcopy

n = int(input())
indegree = [0] * (n + 1)
# 입력 받은 그래프
graph_ = []

# 정점 a에서 b로 이동가능 그래프
graph = [[] for _ in range(n + 1)]

for i in range(n):
     graph_.append(list(map(int, input().split())))


time = [0] * (n + 1)
for index, g in enumerate(graph_):
    time[index + 1] = g[0]
    # 시간 뺴고 나머지 리스트 for 문
    for i in g[1:-1]:
        indegree[index + 1] += 1

        # 정점 i 에서 index로 이동 가능 (i 는 선수 과목)
        graph[i].append(index + 1)

print("graph_", graph_)
print("time", time)
print("graph", graph)
print("indegree", indegree)

def topology_sort():
    result = deepcopy(time)
    q = deque()
    print("result", result)

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])

topology_sort()

