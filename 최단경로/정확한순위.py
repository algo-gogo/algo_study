### 성적 순위를 정확히 알 수 있는 학생은 몇 명인지 계산하는 프로그램 작성
# 입력: 학생들의 수 N, 두 학생의 성적을 비교한 횟수 M
# M개의 줄에는 두 학생의 성적을 비교한 결과를 나타내는 두 양의 정수 A, B
# A번 학생의 성적이 B번 학생보다 낮다.
# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4

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

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(len(graph)):
    print(graph[i])

resultList = []
for a in range(1, n + 1):
    isSafe = False
    for b in range(1, n + 1):
        if graph[a][b] == INF or graph[a][b] == 1 or graph[a][b] == 0:
            pass
        else:
            isSafe = True
    if isSafe:
        resultList.append(a)