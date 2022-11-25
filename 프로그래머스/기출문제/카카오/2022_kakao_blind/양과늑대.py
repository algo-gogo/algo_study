# https://programmers.co.kr/learn/courses/30/lessons/92343

def bfs(start, count, graph):
    # a_count: 0 b_count: 1
    a_count = 1
    b_count = 0
    root = [start]
    while root:
        k = root.pop(0)
        if a_count == b_count:
            break
        if a_count == count:
            break
        for i in graph[k]:
            if i[1] == 0:
                a_count += 1
                root.append(i[0])
            else:
                pass
        break

    return 0

def solution(info, edges):
    answer = 0

    length = len(info)
    graph = [[] for _ in range(length + 1)]

    print(info)
    print(edges)

    count = 0
    for i in info:
        if i == 1:
            count += 1

    for i in range(len(edges)):
        x = edges[i][0]
        y = edges[i][1]
        graph[x].append([y, info[y]])
        graph[y].append([x, info[x]])

    print(graph)

    bfs(0, count, graph)

    return answer


solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
         [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]])

# solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
#          [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]])
