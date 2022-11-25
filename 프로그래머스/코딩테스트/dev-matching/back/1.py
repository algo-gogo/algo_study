# 0 5 2 4 1
# 5 0 3 9 6
# 2 3 0 6 3
# 4 9 6 0 3
# 1 6 3 3 0

# 이런식으로 있을 경우
# 1 -> 2 => 3, 2 -> 0 => 2 ...
# 이렇게 일직선으로 만든다고 했을 경우 위의 그래프를 만족하는 배열
# 1 2 0 4 3
# 3 4 0 2 1

import copy

def solution(dist):
    answer = []
    if len(dist) % 2 == 0:
        l = []
        new_list = []
        for index, value in enumerate(dist[0]):
            new_list.append((value, index))
        new_list.sort()
        for index, value in enumerate(new_list):
            new_index = value[1]
            l.append(new_index)
        print(l)
        answer.append(l)
        copy_l = copy.deepcopy(l)
        copy_l.reverse()
        answer.append(copy_l)
    else:
        l = []
        new_list = []
        print(dist[0])
        for index, value in enumerate(dist[0]):
            new_list.append((value, index))
        new_list.sort()
        del new_list[0]
        print(new_list)
        for i in range(len(new_list) // 2):
            a = new_list[i * 2]
            l.append(a[1])
            l.reverse()
        l.append(0)
        for i in range(len(new_list) // 2):
            a = new_list[i * 2 + 1]
            l.append(a[1])
        print(l)
        copy_l = copy.deepcopy(l)
        copy_l.reverse()
        answer.append(copy_l)
        answer.append(l)

    return answer


print(solution([[0, 5, 2, 4, 1], [5, 0, 3, 9, 6], [2, 3, 0, 6, 3], [4, 9, 6, 0, 3], [1, 6, 3, 3, 0]]))

# print(solution([[0, 2, 3, 1], [2, 0, 1, 1], [3, 1, 0, 2], [1, 1, 2, 0]]))
