# https://programmers.co.kr/learn/courses/30/lessons/42889
# 5스테이지까지밖에 없는데 어떻게 6이지?


def solution(n, stages):
    answer = [[0.0, 0] for _ in range(n)]
    length = len(stages)
    if length == 1:
        return stages[0]
    for i in range(1, n + 1):
        result = 0
        for j in range(len(stages)):
            if i == stages[j]:
                result += 1
        if length != 0:
            answer[i - 1][0] = (result / length)
            answer[i - 1][1] = i
            length -= result
    answer.sort(key=lambda x: x[0], reverse=True)
    answer = sorted(answer, key=lambda x: (-x[0], x[1]))
    resultList = []
    for key, value in answer:
        resultList.append(value)
    return resultList


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
solution(4, [4, 4, 4, 4, 4])
