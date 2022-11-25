# def solution(a, b, m):
#     answer = 0
#
#     graph = [[] for _ in range(len(a) + 2)]
#     for i in range(len(a)):
#         x = a[i][0]
#         y = a[i][1]
#         graph[x].append(y)
#
#     print(graph)
#
#     graph2 = [[] for _ in range(len(b) + 2)]
#     for i in range(len(b)):
#         x = b[i][0]
#         y = b[i][1]
#         graph2[x].append(y)
#
#     print(graph2)
#
#     return answer

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


def union_parent(parent, a, b):
    # a = find_parent(parent, a)
    # b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(a, b, m):
    answer = 0
    parent = [0] * (len(a) + 2)
    for i in range(1, len(a) + 2):
        parent[i] = i
    parent2 = [0] * (len(b) + 2)
    for i in range(1, len(b) + 2):
        parent2[i] = i
    print(parent)
    print(parent2)

    for i in range(len(a)):
        x = a[i][0]
        y = a[i][1]
        union_parent(parent, x, y)

    for i in range(len(b)):
        x = b[i][0]
        y = b[i][1]
        union_parent(parent2, x, y)

    print(parent)
    print(parent2)

    count = 0
    diff_list = []
    for i in range(len(a) + 2):
        if parent[i] == parent2[i]:
            pass
        else:
            diff_list.append([i, parent2[i]])
            count += 1
    print(diff_list)
    for i in diff_list:
        x = i[0]
        y = i[1]


    return count


# print(solution([[1, 2], [2, 3]], [[1, 3], [3, 2]], 1))

print(solution([[1, 2], [3, 1], [2, 4], [3, 5]],
               [[2, 1], [4, 1], [2, 5], [3, 2]],
               1))

# print(solution([[3, 4], [7, 2], [5, 4], [2, 3], [6, 5], [1, 2]],
#                [[2, 1], [3, 6], [1, 4], [1, 5], [7, 1], [3, 2]], 2))
