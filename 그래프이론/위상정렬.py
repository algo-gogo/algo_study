# 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘
# 위상정렬 - 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것

# 예시) 선수과목을 고려한 학습 순서 설정

# 진입차수 : 특정한 노드로 들어오는 간선의 개수
# 진출차수 : 특정한 노드에서 나가는 간선의 개수

# 1. 진입 차수가 0인 노드에 큐를 넣는다.
# 2. 큐가 빌 때까지 과정 반복
# - 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
# - 새롭게 진입차수가 0이 된 노드를 큐에 넣음

# 특징
# DAG에서만 수행가능 (direct acyclic graph) - 순환하지 않는 방향 그래프
# 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단가
# 스택을 이용한 dfs로도 위상정렬 가능
# 여러가지 답이 존재 가능

from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
graph = [[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in graph(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # 정점 A 에서 B 로 이동가능
    # 진입차수 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = []  # 알고리즘 수행 결과를 담을 리스트
    q = deque()  # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 원소꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()