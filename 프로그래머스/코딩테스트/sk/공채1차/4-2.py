from itertools import permutations


def bfs(start, end, n, graph):
    root = [start]
    visited = [0] * (n + 1)
    way = [0] * (n + 1)
    while root:
        k = root.pop(0)
        if k == end:
            break
        if visited[k] == 0:
            visited[k] = 1
            for i in graph[k]:
                root.append(i[0])
                way[i[0]] = way[k] + i[1]
    return way[end]


def solution(n, edges):
    answer = 0
    arr = range(n)
    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        x, y = edge
        graph[x].append([y, 1])

    arr_per_lst = list(permutations(arr, 3))

    for arr_per in arr_per_lst:
        if bfs(arr_per[0], arr_per[1], n, graph) + bfs(arr_per[1], arr_per[2], n, graph) == bfs(arr_per[0], arr_per[2],
                                                                                                n, graph):
            answer += 1
            # print(arr_per)
    return answer


print(solution(5, [[0, 1], [0, 2], [1, 3], [1, 4]]))
