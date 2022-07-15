def solution(grade):

    result = 0
    for i in range(1, len(grade)):
        if grade[i - 1] > grade[i]:
            result += grade[i - 1] - grade[i]


    return result


print(solution([2, 1, 3]))
print(solution([1, 2, 3]))
print(solution([3, 2, 3, 6, 4, 5]))
