# A는 현재 1번 회사에 위치해 있으며, X번 회사에 방문해 물건을 판매
# 연결된 곳은 양방향으로 이동가능
# 소개팅 상대는 k번 회사에 존재한다. A는 X번 회사에 가서 물건을 판매하기 전에 커피마시러 방문
# 결국 A는 1번 회사에서 출발해서 K번 회사를 방문한 뒤 X번 회사로 가는것이 목표

# 입력: 회사의 개수 N, 경로의 개수 M
# 연결된 두 회사의 번호가 공백으로 구분
#

INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# x, k가 공백으로 주어짐 (거쳐갈 노드 x, 목적지 노드 k)
x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)
