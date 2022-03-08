def moveLeft():
    a = 1


def moveRight():
    a = 1


def moveDown():
    a = 1


def moveUp():
    a = 1


def solution(grid):
    resultGraph = [[1, 1, 2, 2],
                   [1, 1, 2, 2],
                   [2, 2, 1, 1],
                   [2, 2, 1, 1]]
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if resultGraph[i][j] == grid[i][j]:
                pass
            else:
                count += 1

    result = count // 2
    if result > 3:
        result += 1

    return result


print(solution([[1, 1, 1, 1],
                [2, 1, 2, 2],
                [2, 2, 2, 1],
                [1, 1, 2, 2]]))

print(solution([[1, 1, 1, 2], [1, 1, 1, 2], [2, 2, 2, 1], [1, 2, 2, 2]]))
