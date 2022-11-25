import heapq

INF = int(1e9)


def solution(n, roads, sources, destination):
    answer = []

    graph = [[] for _ in range(n + 1)]

    for road in roads:
        a = road[0]
        b = road[1]
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    def dijkstra(start, distance):
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

    for s in sources:
        distance = [INF] * (n + 1)
        dijkstra(s, distance)
        distance_destination_ = distance[destination]
        if distance_destination_ == INF:
            answer.append(-1)
        else:
            answer.append(distance_destination_)
    return answer


# print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))
