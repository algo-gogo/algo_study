def solution(alp, cop, problems):
    answer = 0

    maxAlp = 0
    maxCop = 0
    need = []
    for alp, cop, p_alp, p_cop, time in problems:
        l = [alp, cop]
        need.append(l)
        if alp > maxAlp:
            maxAlp = alp
        if cop > maxCop:
            maxCop = cop

    print(maxAlp)
    print(maxCop)
    print(need)

    return answer


# 알고력, 코딩력, 알고 증가력, 코딩 증가력, 문제 푸는데 걸리는 시간

print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
# print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))
