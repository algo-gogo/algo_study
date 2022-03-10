import copy

def move(graph, x1, y1, x2, y2):
    x1 = x1 - 1
    y1 = y1 - 1
    x2 = x2 - 1
    y2 = y2 - 1
    # x가 2라면 오른쪽으로          y가 5라면 아래로
    # x가 5라면 왼쪽으로            y가 2라면 위로
    # x가 2,5도 아니고 y가 5라면 아래로
    # x가 2,5도 아니고 y가 2라면 위로
    graph2 = copy.deepcopy(graph)
    print(graph2)
    minList = []
    for i in range(y2 - y1):
        graph[x1][y2 - i] = graph2[x1][y2 - i - 1]
        minList.append(graph2[x1][y2 - i - 1])
    for i in range(y2 - y1):
        graph[x2][y1 - i - 1] = graph2[x2][y1 - i]
        minList.append(graph2[x2][y1 - i])

    for i in range(x2 - x1):
        graph[x2 - i - 1][y1] = graph2[x2 - i][y1]
        minList.append(graph2[x2 - i][y1])

    for i in range(x2 - x1):
        graph[x1 - i][y2] = graph2[x1 - i - 1][y2]
        minList.append(graph2[x1 - i - 1][y2])

    return min(minList)



def solution(rows, columns, queries):
    answer = []
    graph = [[0 for _ in range(rows)] for _ in range(columns)]

    for i in range(rows):
        for j in range(columns):
            graph[i][j] = (i * columns + j + 1)
    print(graph)
    resultList = []
    for index, value in enumerate(queries):
        resultList.append(move(graph, value[0], value[1], value[2], value[3]))

    return resultList

print(solution(6, 6, [
    [2, 2, 5, 4],
    [3, 3, 6, 6],
    [5, 1, 6, 3]
]))