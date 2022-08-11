def solution(db):
    invite = {}
    for index, d in enumerate(db):
        try:
            invite[d[0]][0] += 1
            invite[d[0]][1] = index
        except:
            invite[d[0]] = [1, index]

    print(invite)

    sort_invite = sorted(invite.items(), key = lambda item: (-item[1][0], item[1][1]))
    print(sort_invite)

    return sort_invite[0][0]


# 직접 초대한 사람 수 * 10 + 내가 초대한 사람이 초대한 사람 수 * 5 + 내가 초대한 사람이 초대한 사람이 초대한 사람수 * 3


print(solution([[1, 2], [2, 3], [2, 4], [2, 5], [5, 6], [5, 7], [6, 8], [2, 9]]))
#
# print(solution([[1, 2], [3, 4]]))
# print(solution([[1, 2], [1, 3], [3, 4], [4, 5], [4, 6], [4, 7]]))
