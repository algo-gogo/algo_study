# https://www.acmicpc.net/problem/18428
# 5
# X S X X T
# T X S X X
# X X X X X
# X T X X X
# X X T X X

n = int(input())

array = []

for i in range(n):
    l = list(map(str, input().split()))
    array.append(l)

# S - 학생, T - 선생님
print(array)


def left(x, y):
    if 0 <= x < n and 0 <= y - 1 < n:
        if array[x][y - 1] == 'O':
            return True
        return left(x, y - 1)
    return False


def right(x, y):
    if 0 <= x < n and 0 <= y + 1 < n:
        if array[x][y + 1] == 'S':
            return True
        return right(x, y + 1)
    return False


def up(x, y):
    if 0 <= x - 1 < n and 0 <= y < n:
        if array[x - 1][y] == 'S':
            return True
        return up(x - 1, y)
    return False


def down(x, y):
    if 0 <= x + 1 < n and 0 <= y < n:
        if array[x + 1][y] == 'S':
            return True
        return down(x + 1, y)
    return False


tList = []
sList = []
for i in range(n):
    for j in range(n):
        if array[i][j] == 'T':
            tList.append((i, j))
        if array[i][j] == 'S':
            sList.append((i, j))

print(tList)
print(sList)

