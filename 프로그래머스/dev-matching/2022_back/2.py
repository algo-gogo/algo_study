def solution(n, horizontal):
    # true - 수평 방향
    answer = [[]]

    # 상 하 좌 우
    horizontal_true = [(-1, 0), (1, 0)]
    horizontal_false = [(0, -1), (0, 1)]

    graph = [[0 for _ in range(n)] for _ in range(n)]
    print(graph)

    graph[0][0] = 1
    present = 1
    x = 0
    y = 0
    # while True:
    #     if horizontal:
    #         for i in horizontal_true:
    #             nx = x + i[0]
    #             ny = y + i[0]
    while True:
        if x == n - 1 and y == n - 1:
            break
        if horizontal:
            y += 1
            present += 1
            horizontal = False
            graph[x][y] = present
        if not horizontal:
            pass





    return answer


print(solution(4, True))
# print(solution(5, False))
