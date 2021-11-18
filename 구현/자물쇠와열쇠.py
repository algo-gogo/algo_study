def isUnLock(keyMoveList, lockList):
    removeList = []

    for i in lockList:
        for j in keyMoveList:
            if i == j:
                removeList.append(i)
                if len(removeList) == len(lockList):
                    return True


def findKey(keyList, lockList):
    length = len(lockList)

    # 큰 사각형으로 봤을 경우 맨 왼쪽 위로 이동
    for i in range(len(keyList)):
        keyList[i][0] = keyList[i][0] - length * 2
        keyList[i][1] = keyList[i][1] - length * 2

    for i in range(length * 2):
        # print( "keyList", keyList)
        for j in range(length * 2):
            keyMoveList = []
            newKeyList = [[0 for _ in range(len(keyList))] for _ in range(len(keyList))]
            for s in range(len(keyList)):
                newKeyList[s][0] = keyList[s][0] + 1
                newKeyList[s][1] = keyList[s][1] + 1
            keyMoveList.append(newKeyList)
            if isUnLock(keyMoveList, lockList):
                return True
        for k in range(len(keyList)):
            keyList[k][0] = keyList[k][0] + 1

    # keyMoveList = []
    # for j in range(length * 2):
    #     for i in range(len(keyList)):
    #         keyList[i][0] = keyList[i][0] + 1
    #         keyList[i][1] = keyList[i][1] + 1
    #     keyMoveList.append(keyList)
    #     if isUnLock(keyMoveList, lockList):
    #         return True
    #     for k in range(length):
    #         keyList[k][0] = keyList[k][0] + 1


def solution(key, lock):
    keyList1 = []
    keyList2 = []
    keyList3 = []
    keyList4 = []
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j] == 1:
                keyList1.append([i, j])
                # 90도 회전
                keyList2.append([-j, i])
                # 180도 회전
                keyList3.append([-i, -j])
                # 270도 회전
                keyList4.append([j, -i])
    lockList = []
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                lockList.append([i, j])

    if findKey(keyList1, lockList):
        return True
    if findKey(keyList2, lockList):
        return True
    if findKey(keyList3, lockList):
        return True
    if findKey(keyList4, lockList):
        return True

    print(keyList1)
    print(keyList2)
    print(keyList3)
    print(keyList4)

    answer = False
    return answer


print(solution(
    [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 1]
    ],
    [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]
))