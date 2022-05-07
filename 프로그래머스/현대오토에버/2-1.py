from collections import deque

import heapq

n = int(input())

INF = int(1e9)

MAX_NUM = 1000000

graph = [[] for i in range(MAX_NUM + 1)]
distance = [INF] * (MAX_NUM + 1)

for i in range(1, MAX_NUM + 1):
    graph[i].append((2 * i, 1))
    graph[i].append(((2 * i) + 1, 1))
    try:
        graph[2 * i].append((i, 1))
        graph[(2 * i) + 1].append((i, 1))
    except:
        pass

# print(graph)
def dijkstra(start, end):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if now == end:
            return dist
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

start_end_list = []
for i in range(n):
    l = list(map(int, input().split()))
    start_end_list.append(l)

result_list = []
for value in start_end_list:
    start = value[0]
    end = value[1]
    result_list.append(dijkstra(start, end))

print(result_list)