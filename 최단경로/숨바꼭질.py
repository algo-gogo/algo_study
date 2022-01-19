# https://www.acmicpc.net/problem/1697

INF = int(1e9)
n, k = map(int, input().split())

maxNK = max(n, k)

graph = [[INF] * (maxNK + 1) for _ in range(maxNK + 1)]

print(graph)