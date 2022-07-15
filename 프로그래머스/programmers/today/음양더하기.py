def solution(absolutes, signs):

    answer = 0
    for index, value in enumerate(absolutes):
        if not signs[index]:
            value = -value
        answer += value

    return answer

print(solution([4, 7, 12], [True, False, True]))