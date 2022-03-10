def solution(lottos, win_nums):
    result = 0
    for i in win_nums:
        for j in lottos:
            if i == j:
                result += 1

    removeNum = 0
    for i in lottos:
        if i == 0:
            removeNum += 1

    print(removeNum)
    print(result)
    #
    # resultList = []
    # if result < 1:
    #     resultList.append(6)
    #     resultList.append(7 - (result + removeNum))
    # else:
    #     resultList.append(7 - result)
    #     resultList.append(7 - (result + removeNum))
    # resultList.sort()
    # return resultList
    maxNum = 7 - (result + removeNum)
    if maxNum > 5:
        maxNum = 6
    minNum = 7 - result
    if minNum > 5:
        minNum = 6

    resultList = []
    resultList.append(maxNum)
    resultList.append(minNum)
    return resultList



print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))

print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))

print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))