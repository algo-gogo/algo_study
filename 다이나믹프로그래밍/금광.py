# 오른쪽, 오른쪽 위, 오른쪽 아래
dx = [0, -1, 1]
dy = [1, 1, 1]
def solution(n, m, array):
    print(array)
    for i in range(1, m):
        for j in range(n):
            if j == 0:
                array[j][i] += max(array[j][i - 1], array[j + 1][i - 1])
            elif j == n - 1:
                array[j][i] += max(array[j][i - 1], array[j - 1][i - 1])
            else:
                array[j][i] += max(array[j][i - 1], array[j - 1][i - 1], array[j + 1][i - 1])

    print(array[n - 1])
    print(max(array[n - 1]))



testCase = int(input())

for i in range(testCase):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    nList = []
    index = 0
    for j in range(n):
        nList.append(l[index: index + m])
        index += m
    solution(n, m, nList)
