def dfs(x, y, graph, row, column):
    result = 0
    if x >= 0 and x < column and y >= 0 and y < row:
        if graph[x][y] == 2:
            result += 1
            graph[x][y] = 3
            result += dfs(x - 1, y, graph, row, column)
            result += dfs(x + 1, y, graph, row, column)
            result += dfs(x, y - 1, graph, row, column)
            result += dfs(x, y + 1, graph, row, column)

    return result

def solution(rows, columns, lands):
    graph = [[0 for _ in range(columns)] for _ in range(rows)]
    print(graph)

    for land in lands:
        graph[land[0] - 1][land[1] - 1] = 1

    print(graph)
    for i in range(2, rows - 2):
        land_list = graph[i]
        index_list = []
        for index, value in enumerate(land_list):
            if value == 1:
                index_list.append(index)
                break
        for land in range(len(land_list) - 1, -1, -1):
            if land_list[land] == 1:
                index_list.append(land)
                break

        for j in range(index_list[0], index_list[1]):
            if land_list[j] == 0:
                land_list[j] = 2

    print(graph)

    # 개수세기
    answer = []
    for i in range(rows):
        for j in range(columns):
            if graph[i][j] == 2:
                answer.append(dfs(i, j, graph, rows, columns))

    print(answer)
    result = []
    if len(answer) == 0:
        return [-1, -1]
    else:
        result.append(min(answer))
        result.append(max(answer))
        return result


print(solution(9, 7,
               [[2, 2], [2, 3], [2, 5], [3, 2], [3, 4], [3, 5], [3, 6], [4, 3], [4, 6], [5, 2], [5, 5], [6, 2], [6, 3],
                [6, 4], [6, 6], [7, 2], [7, 6], [8, 3], [8, 4], [8, 5]]))

print(solution(5, 6,
               [[2, 2], [2, 3], [2, 4], [3, 2], [3, 5], [4, 3], [4, 4]]))

print(solution(5, 7,
               [[2, 5], [3, 3], [3, 4], [3, 5], [4, 3]]))
