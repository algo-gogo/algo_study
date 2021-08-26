t = int(input())

resultList = []

def dfs(x, y):
    if x >= 0 and x < n and y >= 0 and y < m:
        if matrix[x][y] == 0:
            matrix[x][y] = 1
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
        else:
            return False

for _ in range(t):
    m, n, k = map(int, input().split())

    matrix = [[1] * m for _ in range(n)]

    for i in range(k):
        a, b = map(int, input().split())
        matrix[b][a] = 0

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                result += 1

    resultList.append(result)

for i in resultList:
    print(i)
