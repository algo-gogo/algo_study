def solution(survey, choices):
    answer = ''
    # N: 1 C: 1 M: 2 T: 3 A: 1
    # T C M A

    mbti = {1: 'RT', 2: 'CF', 3: 'JM', 4: 'AN'}
    choice = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    result = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(len(survey)):
        m = survey[i]
        c = choices[i]
        if c in [1, 2, 3]:
            result[m[0]] += choice[c]
        else:
            result[m[1]] += choice[c]

    print(result)
    # for i in enumerate(result.items()):
    #     print(i)
    resultList = list(result.items())
    print(resultList)
    for i in range(4):
        first = resultList[i * 2][1]
        second = resultList[i * 2 + 1][1]
        if first >= second:
            answer += resultList[i * 2][0]
        else:
            answer += resultList[i * 2 + 1][0]

    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
# print(solution(["TR", "RT", "TR"], [7, 1, 3]))
