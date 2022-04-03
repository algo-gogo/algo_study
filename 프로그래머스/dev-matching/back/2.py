from itertools import permutations
from itertools import combinations

import copy


def dfs(x, y, alpha, n, graph):
    if 0 <= x < n and 0 <= y < n:
        if graph[x][y] == alpha:
            graph[x][y] = 3
            dfs(x - 1, y, alpha, n, graph)
            dfs(x + 1, y, alpha, n, graph)
            dfs(x, y - 1, alpha, n, graph)
            dfs(x, y + 1, alpha, n, graph)
            return 1
        else:
            return 0
    return 0


def find_link(graph):
    result = 0
    a_count = 0
    b_count = 0
    c_count = 0
    first_list = []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 'a':
                if a_count == 0:
                    first_list.append((i, j))
                a_count += 1
            if graph[i][j] == 'b':
                if b_count == 0:
                    first_list.append((i, j))
                b_count += 1
            if graph[i][j] == 'c':
                if c_count == 0:
                    first_list.append((i, j))
                c_count += 1
    count_list = []
    count_list.append(a_count)
    count_list.append(b_count)
    count_list.append(c_count)
    count = 0
    prev = 0
    answer = []
    for index, value in enumerate(first_list):
        alpha = 'a'
        if index == 0:
            alpha = 'a'
        if index == 1:
            alpha = 'b'
        if index == 2:
            alpha = 'c'
        for i in range(len(graph)):
            for j in range(len(graph)):
                if dfs(value[0], value[1], alpha, len(graph), graph):
                    now = 0
                    count += 1
                    for k in range(len(graph)):
                        now += graph[k].count(3)
                    now -= prev
                    answer.append(now)
                    prev += now
    if answer == count_list:
        return 1
    return 0


def solution(grid):
    graph = []

    q_count = 0
    q_array = []
    for i in range(len(grid)):
        l = []
        for index, j in enumerate(grid[i]):
            l.append(j)
            if j == '?':
                q_count += 1
                q_array.append((i, index))
        graph.append(l)

    q_list = ['a', 'b', 'c'] * q_count
    permutation_list = list(combinations(q_list, q_count))
    answer = 0


    for index, value in enumerate(permutation_list):
        copy_graph = copy.deepcopy(graph)
        for i in range(len(q_array)):
            q_value = q_array[i]
            x = q_value[0]
            y = q_value[1]
            copy_graph[x][y] = value[i]

        answer += find_link(copy_graph)

    return answer


print(solution(["??b", "abc", "cc?"]))
# print(solution(["abcabcab", "????????"]))
# print(solution(["aa?"]))
