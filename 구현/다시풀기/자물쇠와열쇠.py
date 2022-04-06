import copy

def make_key_list(key):
    key_list = []
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j] == 1:
                key_list.append([i, j])
    return key_list

def turn_90(key_list):
    n = len(key_list)
    m = len(key_list[0])
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[j][n - i - 1] = key_list[i][j]

    return new

def find_result(graph, key_list, length):
    for i in range(length * 2):
        for j in range(length * 2):
            copy_graph = copy.deepcopy(graph)
            copy_key_list = copy.deepcopy(key_list)
            for copy_key in copy_key_list:
                copy_key[0] += i
                copy_key[1] += j

            # for copy_key in copy_key_list:
            #     copy_key[0] += i
            #     copy_key[1] += j

            for key in copy_key_list:
                x = key[0]
                y = key[1]
                print("x", x)
                print("y", y)
                print(copy_key_list)
                copy_graph[x][y] = 1

            if check_all(copy_graph, length):
                return True


def check_all(copy_graph, length):
    for i in range(length, length * 2):
        for j in range(length, length * 2):
            if copy_graph[i][j] == 0:
                return False
    return True


def solution(key, lock):
    print(lock)
    length = len(lock)

    # 원본 그대로
    key2 = turn_90(key)
    key3 = turn_90(key2)
    key4 = turn_90(key3)

    key_list = make_key_list(key)
    key_list2 = make_key_list(key2)
    key_list3 = make_key_list(key3)
    key_list4 = make_key_list(key4)

    graph = [[1 for _ in range(length * 3)] for _ in range(length * 3)]
    for i in range(length):
        for j in range(length):
            graph[length + i][length + j] = lock[i][j]

    if find_result(graph, key_list, length):
        return True
    if find_result(graph, key_list2, length):
        return True
    if find_result(graph, key_list3, length):
        return True
    if find_result(graph, key_list4, length):
        return True

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
               [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

# [:] 1차원 배열은 가능 이차원 배열은 deepcopy 불가능
