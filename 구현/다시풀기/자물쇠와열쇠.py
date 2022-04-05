import copy

def check_all(copy_graph, length):
    for i in range(length, length * 2):
        for j in range(length, length * 2):
            if copy_graph[i][j] == 0:
                return False
    return True

def solution(key, lock):
    answer = True

    print(key)
    print(lock)
    length = len(lock)

    key_list = []
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j] == 1:
                key_list.append([i, j])

    # 원본 그대로
    print(key_list)

    graph = [[1 for _ in range(length * 3)] for _ in range(length * 3)]
    for i in range(length):
        for j in range(length):
            graph[length + i][length + j] = lock[i][j]

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


    print(graph)

    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
               [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

# [:] 1차원 배열은 가능 이차원 배열은 deepcopy 불가능