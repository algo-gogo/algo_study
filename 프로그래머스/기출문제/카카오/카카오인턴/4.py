# from collections import deque
# import copy
#
# def bfs(graph, start, end, visited):
#     queue = deque()
#     queue.append((start))
#     print(queue)
#     min_list = []
#     while queue:
#         popleft = queue.popleft()
#         for i in graph[popleft]:
#             if not visited[i[0]]:
#                 queue.append(i[0])
#                 min_list.append(i[1])
#                 visited[i[0]] = True
#
#     return max(min_list)
#
# def solution(n, paths, gates, summits):
#     graph = [[] for _ in range(n + 1)]
#
#     for i in range(len(paths)):
#         x = paths[i][0]
#         y = paths[i][1]
#         graph[x].append([y, paths[i][2]])
#         graph[y].append([x, paths[i][2]])
#
#     print(graph)
#     print(gates)
#     print(summits)
#     result_list = []
#     for i in gates:
#         for j in summits:
#             copy_gate = copy.deepcopy(gates)
#             copy_gate.remove(i)
#             copy_summits = copy.deepcopy(summits)
#             copy_summits.remove(j)
#             visited = [False for _ in range(len(graph))]
#             for a in copy_gate:
#                 visited[a] = True
#             # for a in copy_summits:
#             #     visited[a] = True
#             visited[j] = True
#             result_list.append([j, bfs(graph, i, j, visited)])
#             # result_list.append([j, dfs(graph, i, j, visited, min_list)])
#
#     print(result_list)
#     result_list.sort(key=lambda x: x[1])
#
#     return result_list[0]

import copy


def check(graph, start, end, visited):
    root = [start]
    copy_visited = copy.deepcopy(visited)
    while root:
        k = root.pop(0)
        if k == end:
            return True
        for i in graph[k]:
            if not copy_visited[i[0]]:
                root.append(i[0])
                copy_visited[i[0]] = True
    return False


def dfs(graph, start, end, visited, min_list):
    graph[start].sort(key=lambda x: x[1])
    for i in graph[start]:
        if not visited[i[0]]:
            if check(graph, start, end, visited):
                min_list.append(i[1])
                return dfs(graph, i[0], end, visited, min_list)

    return max(min_list)


def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]

    for i in range(len(paths)):
        x = paths[i][0]
        y = paths[i][1]
        graph[x].append([y, paths[i][2]])
        graph[y].append([x, paths[i][2]])

    result_list = []
    for i in gates:
        for j in summits:
            copy_gate = copy.deepcopy(gates)
            copy_gate.remove(i)
            copy_summits = copy.deepcopy(summits)
            copy_summits.remove(j)
            visited = [False for _ in range(len(graph))]
            for a in copy_gate:
                visited[a] = True
            # for a in copy_summits:
            #     visited[a] = True
            min_list = []
            result_list.append([j, dfs(graph, i, j, visited, min_list)])

    print(result_list)
    result_list.sort(key=lambda x: x[1])

    return result_list[0]


print(
    solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
# print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
# print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
# print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))
