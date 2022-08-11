import math

def solution(levels):

    levels.sort(reverse=True)
    print(levels)
    length = len(levels)
    num = length * 0.25
    print(math.trunc(num))

    result_list = []
    for i in range(math.trunc(num)):
        result_list.append(levels[i])

    return min(result_list)


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))
