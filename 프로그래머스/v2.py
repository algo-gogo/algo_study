# 세로
import copy

def find_h(graph, n):
    result = 0
    for i in range(len(graph[0])):
        count = 0
        for j in range(len(graph)):
            a = graph[j][i]
            if a == 1:
                count += 1
            else:
                if count == n:
                    result += 1
                count = 0
        if count == n:
            result += 1
    return result


# 가로
def find_w(graph, n):
    result = 0
    for i in range(len(graph)):
        value = graph[i]
        count = 0
        for index, j in enumerate(value):
            if j == 1:
                count += 1
            else:
                if count == n:
                    result += 1
                count = 0
        if count == n:
            result += 1
    return result

# 대각선
def find_a(graph, n):
    # lenW = len(graph)
    # lenH = len(graph[0])
    # result = 0
    # for i in range(len(graph)):
    #     value = graph[i]
    #     count = 0
    #     for j in range(len(value) - i - (lenH - lenW)):
    #         value = graph[i][j]
    #         if j == 0:
    #             count += 1
    #         else:
    #             if count == n:
    #                 result += 1
    #             count = 0
    #     if count == n:
    #         result += 1
    # return result
    return 4


def solution(h, w, n, board):
    graph = [[0 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            graph[i][j] = int(board[i][j])

    print(graph)
    resultH = find_h(graph, n)
    resultW = find_w(graph, n)
    print(resultH, resultW)
    resultA = find_a(graph, n)
    print(resultA)

    return resultA + resultW + resultH


print(solution(7, 9, 4, ["111100000", "000010011", "111100011", "111110011", "111100011", "111100010", "111100000"]))
