def solution(paths):
    forward_lst, back_lst = [], []
    for path in paths:
        if path[0] < path[1]:  # forward
            if not path[0] in forward_lst and not path[1] in forward_lst:
                forward_lst.extend(path)
            elif path[0] in forward_lst:
                forward_lst.remove(path[0])
                forward_lst.append(path[1])
            elif path[1] in forward_lst:
                forward_lst.remove(path[1])
                forward_lst.append(path[0])
        else:  # backward
            if not path[0] in back_lst and not path[1] in back_lst:
                back_lst.extend(path)
            elif path[0] in back_lst:
                back_lst.remove(path[0])
                back_lst.append(path[1])
            elif path[1] in back_lst:
                back_lst.remove(path[1])
                back_lst.append(path[0])
    forward_lst.sort()
    back_lst.sort(reverse=True)

    answer = []
    for i in range(0, len(forward_lst), 2):
        fl2 = forward_lst[i:i + 2]
        answer.append(fl2)

    for i in range(0, len(back_lst), 2):
        bl2 = back_lst[i:i + 2]
        answer.append(bl2)

    answer.sort()
    print(answer)
    answer2 = sum(answer, [])
    return answer2


print(solution([[1, 2], [2, 3], [3, 4], [8, 7], [7, 6]]))
# print(solution([[1, 2], [4, 5], [10, 9], [3, 4]]))
# print(solution([[1, 2], [10, 9], [11, 12], [12, 13]]))
