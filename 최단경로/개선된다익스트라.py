# 시간 복잡도 O(ElogV)   - v(노드의 개수) ,e (간선의 개수)
# 힙 자료구조를 사용한다
# 힙 - 우선순위 큐를 구현하기 위하여 사용하는 자료구조중 하나
# 우선순위 큐- 가장 우선순위가 높은 데이터 추출

# 파이썬에서 우선순위 큐를 사용할 때 heapq를 사용함
# ex) 가치와 물건으로 묶어서 우선순위 큐 자료구조에 넣고 가치로 우선순위를 결정

# 내부적으로 최소힙, 최대 힙을 이용한다
# 최소힙은 값이 낮은 데이터가 먼저 삭제, 최대 힙은 값이 큰 데이터가 먼저 삭제
# 보통 최소힙을 사용한다. 최대힙을 사용할 떄는 - 붙여서 사용

import heapq
import sys
input =sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
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

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

