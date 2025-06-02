import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


def get_min_city_chicken_distance(n, m, city_map):

    chicken_list = []
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 2:
                chicken_list.append((i, j))
    home_list = []
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                home_list.append((i, j))

    p_chicken_list = list(itertools.permutations(chicken_list, m))
    print(p_chicken_list)

    distance_list = []
    for p_chicken in p_chicken_list:
        distance = 0
        for home in home_list:
            min_distance = 9999999
            for chicken in p_chicken:
                home_to_chicken = abs(home[0] - chicken[0]) + abs(home[1] - chicken[1])
                if min_distance > home_to_chicken:
                    min_distance = home_to_chicken
            distance += min_distance
        distance_list.append(distance)

    return min(distance_list)


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!


city_map = [
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0]
]
print("정답 = 11 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,1,city_map))


city_map = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2, 2, 0, 1, 2]
]
print("정답 = 10 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,2,city_map))