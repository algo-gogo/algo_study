def shift_row(graph):
    copy_graph = [item[:] for item in graph]
    for i in range(len(graph)):
        graph[i] = copy_graph[i - 1]
    return graph


# def rotate(graph):
#     copy_graph = copy.deepcopy(graph)
#     # 가로
#     for i in range(len(graph[0]) - 1):
#         graph[0][i + 1] = copy_graph[0][i]
#     for i in range(len(graph[0]) - 1, 0, -1):
#         graph[len(graph) - 1][i - 1] = copy_graph[len(graph) - 1][i]
#
#     # 세로
#     for i in range(len(graph) - 1, 0, -1):
#         graph[i - 1][0] = copy_graph[i][0]
#     for i in range(len(graph) - 1):
#         graph[i + 1][len(graph[0]) - 1] = copy_graph[i][len(graph[0]) - 1]
#
#     return graph

def rotate(graph):
    ar, ac = 0, 0
    br, bc = len(graph) - 1, len(graph[0]) - 1
    for i in range(bc-1, ac-1, -1):
        graph[ar][i], graph[ar][i + 1] = graph[ar][i + 1], graph[ar][i]
    for i in range(ar, br):
        graph[i][ac], graph[i + 1][ac] = graph[i + 1][ac], graph[i][ac]
    for i in range(ac, bc):
        graph[br][i], graph[br][i+1] = graph[br][i+1], graph[br][i]
    for i in range(br-1, ar, -1):
        graph[i][bc], graph[i+1][bc] = graph[i+1][bc], graph[i][bc]
    return graph


def solution(rc, operations):
    answer = [[]]

    for operation in operations:
        if operation == "Rotate":
            rc = rotate(rc)
            print(rc)
        else:
            rc = shift_row(rc)
            print(rc)
    print("result", rc)
    return rc


# print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))
# print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))
