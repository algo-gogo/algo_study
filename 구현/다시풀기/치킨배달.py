from itertools import combinations

n, m = map(int, input().split())

graph = []
for i in range(n):
    l = list(map(int, input().split()))
    graph.append(l)

# 1: 집
# 2: 치킨집
print(graph)

chicken_list = []
home_list = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken_list.append([i, j])
        if graph[i][j] == 1:
            home_list.append([i, j])

new_chicken_list = list(combinations(chicken_list, m))
print(chicken_list)
print(home_list)
print(new_chicken_list)

result_list = []
# for new_chicken in new_chicken_list:
#     result = 0
#     for chicken in new_chicken:
#         distance_list = []
#         for home in home_list:
#             distance = abs(chicken[0] - home[0]) + abs(chicken[1] - home[1])
#             distance_list.append(distance)
#         print("distance_list", sum(distance_list))
#         result += min(distance_list)
#     result_list.append(result)

new_result_list = []
for new_chicken in new_chicken_list:
    result = 0
    result_list = []
    for home in home_list:
        distance_list = []
        for chicken in new_chicken:
            distance = abs(chicken[0] - home[0]) + abs(chicken[1] - home[1])
            distance_list.append(distance)
        result_list.append(min(distance_list))
    new_result_list.append(result_list)

print(new_result_list)
min_result = []
for i in new_result_list:
    min_result.append(sum(i))

print(min(min_result))