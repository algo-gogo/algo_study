import heapq
import sys

# 노드의 개수와 간선의 개수
n, m = map(int, sys.stdin.readline().split())

INF = int(1e9)
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))


v1, v2 = map(int, sys.stdin.readline().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(1)
result = distance[v1]

dijkstra(v1)
result += distance[v2]

dijkstra(v2)
result += distance[n]

print(result)