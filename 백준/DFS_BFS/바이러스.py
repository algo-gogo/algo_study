# 컴퓨터의 수,  컴퓨터들끼리의 연결 수
n = int(input())

m = int(input())

matrix = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    m1, m2 = map(int, input().split())
    matrix[m1][m2] = matrix[m2][m1] = 1


result = []

def dfs(start, visited=[]):
    visited.append(start)
    result.append(start)

    for w in range(len(matrix[start])):
        if matrix[start][w] == 1 and (w not in visited):
            dfs(w, visited)


dfs(1)
print(len(result) - 1)