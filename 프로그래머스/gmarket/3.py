# def bfs(start, end, n, graph):
#     root = [start]
#     way = [0] * (n + 1)
#     while root:
#         k = root.pop(0)
#         if k == end:
#             break
#         for i in graph[k]:
#             root.append(i[0])
#             way[i[0]] = way[k] + i[1]
#     return way[end]

def bfs(start, end, graph):
    print(graph)
    print(start)
    print(end)
    count = 0
    root = [start]
    while root:
        k = root.pop(0)
        if k == end:
            count += 1
        for i in graph[k]:
            root.append(i)
    return count


def solution(depar, hub, dest, roads):
    city_list = []
    for i in roads:
        for j in i:
            city_list.append(j)

    city_list = list(set(city_list))
    city_dic = {}
    for index, value in enumerate(city_list):
        city_dic[value] = index

    print(city_dic)
    graph = [[] for _ in range(len(city_list) + 1)]

    for i in range(len(roads)):
        city_depart = roads[i][0]
        city_dest = roads[i][1]
        x = city_dic[city_depart]
        y = city_dic[city_dest]
        graph[x].append(y)

    depar_ = city_dic[depar]
    hub_ = city_dic[hub]
    dest_ = city_dic[dest]
    one = bfs(depar_, hub_, graph)
    two = bfs(hub_, dest_, graph)
    return one * two % 10007


print(solution("SEOUL", "DAEGU", "YEOSU",
               [["ULSAN", "BUSAN"], ["DAEJEON", "ULSAN"], ["DAEJEON", "GWANGJU"], ["SEOUL", "DAEJEON"],
                ["SEOUL", "ULSAN"], ["DAEJEON", "DAEGU"], ["GWANGJU", "BUSAN"], ["DAEGU", "GWANGJU"],
                ["DAEGU", "BUSAN"], ["ULSAN", "DAEGU"], ["GWANGJU", "YEOSU"], ["BUSAN", "YEOSU"]]))

# print(solution("ULSAN", "SEOUL", "BUSAN",
#                [["SEOUL", "DAEJEON"], ["ULSAN", "BUSAN"], ["DAEJEON", "ULSAN"], ["DAEJEON", "GWANGJU"],
#                 ["SEOUL", "ULSAN"], ["DAEJEON", "BUSAN"], ["GWANGJU", "BUSAN"]]))
