def solution(n):
    answer = []

    value = 0
    for i in range(n):
        value += i + 1
        answer.append([0] * (i + 1))

    value2 = 0
    # for i in range(len(answer)):
    #     for j in range(len(answer[i])):
    #         value2 += 1
    #         answer[i][j] = value2

    return answer

print(solution(4))
print(solution(5))
print(solution(6))