### BFS 문제
# 특정 도시 X 로부터 출발하여 도달할 수 있는 모든 도시 중에서 최단 거리가 정확히 k 인 도시들의 번호 출력
# 입력: 도시의 개수 N , 도로의 개수 M, 거리 정보 K, 출발 도시 번호 X
#      M개의 줄에 걸쳐서 A에서 B로 가는 단방향 도로
# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4

from collections import deque

n, m, k, x = map(int, input().split())

array = []
for i in range(m):
    array.append(list(map(int, input().split())))


def bfs(city):
    queue = deque()
    queue.append(city)
    distance = 0
    while queue:
        start = queue.popleft()
        for a in array:
            if a[0] + 1 == start:
                distance += 1
                queue.append(a[1] + 1)

    return distance


resultList = []
for i in range(n):
    if bfs(n) == k:
        resultList.append(n)

if len(resultList) == 0:
    print(-1)
else:
    for i in resultList:
        print(i, end=' ')
