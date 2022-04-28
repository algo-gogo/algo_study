import copy


def move(graph, x1, y1, x2, y2):
    x1 = x1 - 1  # 1
    y1 = y1 - 1  # 1
    x2 = x2 - 1  # 4
    y2 = y2 - 1  # 3
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
        graph[x2][y2 - i - 1] = graph2[x2][y2 - i]
        minList.append(graph2[x2][y1 - i])

    for i in range(x2 - x1):
        graph[x2 - i - 1][y1] = graph2[x2 - i][y1]
        minList.append(graph2[x2 - i][y1])

    for i in range(x2 - x1):
        graph[x2 - i][y2] = graph2[x2 - i - 1][y2]
        minList.append(graph2[x2 - i - 1][y2])

    return (graph, min(minList))


def solution(rows, columns, queries):
    graph = [[0 for _ in range(columns)] for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            graph[i][j] = (i * columns + j + 1)
    print(graph)
    result_list = []
    for index, value in enumerate(queries):
        graph, min_num = move(graph, value[0], value[1], value[2], value[3])
        result_list.append(min_num)

    return result_list


# print(solution(6, 6, [
#     [2, 2, 5, 4],
#     [3, 3, 6, 6],
#     [5, 1, 6, 3]
# ]))

# print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
print(solution(100, 97, [[1, 1, 100, 97]]))


####################### 답지
# def make_matrix(rows, columns):
#     matrix = [[0] * columns for _ in range(rows)]
#     for i in range(1, rows + 1):
#         for j in range(1, columns + 1):
#             matrix[i - 1][j - 1] = (columns * (i - 1)) + j
#
#     return matrix
#
# def rotate(queries, matrix):
#     ar, ac, br, bc = queries
#     mins = []
#     ar -= 1
#     ac -= 1
#     br -= 1
#     bc -= 1
#     for i in range(bc-1, ac-1, -1):
#         matrix[ar][i], matrix[ar][i + 1] = matrix[ar][i + 1], matrix[ar][i]
#         mins.append(matrix[ar][i])
#         mins.append(matrix[ar][i + 1])
#     for i in range(ar, br):
#         matrix[i][ac], matrix[i + 1][ac] = matrix[i + 1][ac], matrix[i][ac]
#         mins.append(matrix[i][ac])
#         mins.append(matrix[i + 1][ac])
#     for i in range(ac, bc):
#         matrix[br][i], matrix[br][i+1] = matrix[br][i+1], matrix[br][i]
#         mins.append(matrix[br][i])
#         mins.append(matrix[br][i+1])
#     for i in range(br-1, ar, -1):
#         matrix[i][bc], matrix[i+1][bc] = matrix[i+1][bc], matrix[i][bc]
#         mins.append(matrix[i][bc])
#         mins.append(matrix[i+1][bc])
#     mins = set(mins)
#     return (matrix, min(mins))
#
#
# def solution(rows, columns, queries):
#     matrix = make_matrix(rows, columns)
#     result = []
#     for q in queries:
#         matrix, MIN = rotate(q, matrix)
#         result.append(MIN)
#     return result
# print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))