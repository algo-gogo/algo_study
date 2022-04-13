# https://programmers.co.kr/learn/courses/30/lessons/60059

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
            print("copy_key_list", copy_key_list)
            for copy_key in copy_key_list:
                copy_key[0] += i
                copy_key[1] += j

            for key in copy_key_list:
                x = key[0]
                y = key[1]
                print("x", x)
                print("y", y)
                print(copy_key_list)
                # 겹치는 부분 +1 해줘서
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
    print("lock", lock)
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
#
#
# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
#                [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

# [:] 1차원 배열은 가능 이차원 배열은 deepcopy 불가능

### 유진씨꺼
# def turn(array):
#     length = len(array)
#     temp = [[[] for j in range(length)] for i in range(length)]
#     positions = []
#     for i in range(length):
#         for j in range(length):
#             temp[i][j] = array[j][length - i - 1]
#             if (temp[i][j]):
#                 positions.append([i, j])
#     return temp, positions
#
#
# def match(array, destination, positions_key, positions_lock):
#     if (len(positions_lock) == 0):
#         return True
#     elif (len(positions_key) < len(positions_lock)):
#         return False
#
#     for key in positions_key:
#         for lock in positions_lock:
#             i = lock[0] - key[0]
#             j = lock[1] - key[1]
#
#             matched = 0
#             for temp_key in positions_key:
#                 temp_i = temp_key[0] + i
#                 temp_j = temp_key[1] + j
#
#                 try:
#                     if destination[temp_i][temp_j] == 0:
#                         matched += 1
#                     else:
#                         matched = -1
#                         break
#
#                 except:
#                     continue
#             if (matched == len(positions_lock)):
#                 return True
#     return False
#
#
# def solution(key, lock):
#     lock_size = len(lock)
#     key_size = len(key)
#     lock_position = []
#
#     for i in range(lock_size):
#         for j in range(lock_size):
#             if (lock[i][j] == 0):
#                 lock_position.append([i, j])
#
#     temp = key
#
#     temp_position = []
#
#     for i in range(key_size):
#         for j in range(key_size):
#             if (key[i][j]):
#                 temp_position.append([i, j])
#
#     for i in range(4):
#         if (match(temp, lock, temp_position, lock_position)):
#             return True
#         temp, temp_position = turn(temp)
#
#     return False


# print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print( solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[0, 1, 1], [1, 1, 1], [1, 1, 1]]))