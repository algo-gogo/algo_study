# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def move(graph, index, num):
    num1 = num
    num2 = num
    num3 = num
    num4 = num
    for i in range(index, len(graph) - index - 1):
        graph[index][i] = num1
        num1 += 1
    for i in range(index, len(graph) - index - 1):
        graph[i][len(graph) - 1 - index] = num2
        num2 += 1
    for i in range(len(graph) - 1 - index, index, -1):
        graph[len(graph) - 1 - index][i] = num3
        num3 += 1
    for i in range(len(graph) - 1 - index, index, -1):
        graph[i][index] = num4
        num4 += 1

    return num1

def move2(graph, index, num):
    num1 = num
    num2 = num
    num3 = num
    num4 = num
    for i in range(len(graph) - 1 - index, index, -1):
        graph[index][i] = num1
        num1 += 1
    for i in range(index, len(graph) - index - 1):
        graph[i][index] = num2
        num2 += 1
    for i in range(index, len(graph) - index - 1):
        graph[len(graph) - 1 - index][i] = num3
        num3 += 1
    for i in range(len(graph) - 1 - index, index, -1):
        graph[i][len(graph) - 1 - index] = num4
        num4 += 1

    return num1


def solution(n, clockwise):
    result_list = [[0 for i in range(n)] for i in range(n)]
    print(result_list)

    num1 = 1
    if clockwise:
        if n % 2 == 0:
            for i in range(n // 2):
                num1 = move(result_list, i, num1)
        else:
            for i in range(n // 2 + 1):
                num1 = move(result_list, i, num1)
            result_list[n // 2][n // 2] = num1
    else:
        if n % 2 == 0:
            for i in range(n // 2):
                num1 = move2(result_list, i, num1)
        else:
            for i in range(n // 2 + 1):
                num1 = move2(result_list, i, num1)
            result_list[n // 2][n // 2] = num1

    print(result_list)
    return result_list


print(solution(5, True))
print(solution(6, True))
print(solution(6, False))
print(solution(9, False))
