INF = int(1e9)


def solution(n, s, a, b, fares):
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0

    for index, value in enumerate(fares):
        x = value[0]
        y = value[1]
        v = value[2]
        graph[x][y] = v
        graph[y][x] = v

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != j:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                    graph[j][i] = graph[i][j]

    print(graph)

    t_distance_list = []
    for t in range(1, n + 1):
        d1 = graph[s][t]
        d2 = graph[t][a]
        d3 = graph[t][b]
        t_distance = d1 + d2 + d3
        t_distance_list.append(t_distance)

    t_min_distance = min(t_distance_list)
    each_distance = graph[s][a] + graph[s][b]
    print(t_min_distance)
    print(each_distance)

    return min(t_min_distance, each_distance)


# print(solution(6, 4, 6, 2, [
#     [4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]
# ]))

# print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
#
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))
