# https://www.acmicpc.net/problem/18428
# 5
# X S X X T
# T X S X X
# X X X X X
# X T X X X
# X X T X X

from itertools import combinations
import copy

n = int(input())

array = []

for i in range(n):
    l = list(map(str, input().split()))
    array.append(l)

arrayCopy = copy.deepcopy(array)
# S - 학생, T - 선생님
print(array)


### True - 감시 피할 수 있음
### False - 감시 피할 수 없음
def left(x, y):
    if 0 <= x < n and 0 <= y - 1 < n:
        if arrayCopy[x][y - 1] == 'O':
            return True
        if arrayCopy[x][y - 1] == 'S':
            return False
        return left(x, y - 1)
    return True


def right(x, y):
    if 0 <= x < n and 0 <= y + 1 < n:
        if arrayCopy[x][y + 1] == 'O':
            return True
        if arrayCopy[x][y + 1] == 'S':
            return False
        return right(x, y + 1)
    return True


def up(x, y):
    if 0 <= x - 1 < n and 0 <= y < n:
        if arrayCopy[x - 1][y] == 'O':
            return True
        if arrayCopy[x - 1][y] == 'S':
            return False
        return up(x - 1, y)
    return True


def down(x, y):
    if 0 <= x + 1 < n and 0 <= y < n:
        if arrayCopy[x + 1][y] == 'O':
            return True
        if arrayCopy[x + 1][y] == 'S':
            return False
        return down(x + 1, y)
    return True


xList = []
for i in range(n):
    for j in range(n):
        if array[i][j] == 'X':
            xList.append((i, j))
selectXList = list(combinations(xList, 3))
print(selectXList)

resultList = []
for selectX in selectXList:
    arrayCopy = copy.deepcopy(array)
    for x, y in selectX:
        arrayCopy[x][y] = 'O'

    for i in range(n):
        for j in range(n):
            if arrayCopy[i][j] == 'T':
                resultList.append(right(i, j))
                resultList.append(left(i, j))
                resultList.append(up(i, j))
                resultList.append(down(i, j))
