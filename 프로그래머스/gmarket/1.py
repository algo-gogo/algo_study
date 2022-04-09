def count(x, y, maps):
    if -1 < x < len(maps) and -1 < y < len(maps[0]):
        return 1 if (maps[x][y] == 0) else 0
    return 1


def solution(maps):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    x_len = len(maps)
    y_len = len(maps[0])
    result = 0

    for i in range(x_len):
        for j in range(y_len):
            if maps[i][j] == 1:
                for index in range(4):
                    result += count(i + dx[index], j + dy[index], maps)

    return result


print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 1], [0, 0, 1, 0, 1], [1, 1, 1, 0, 1]]))
# print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 0, 0]]))

print(solution([[1, 0, 1, 1], [0, 0, 1, 1], [1, 1, 0, 1], [1, 1, 0, 0]]))
