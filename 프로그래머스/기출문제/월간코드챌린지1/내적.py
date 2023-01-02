def solution(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]

    return result


print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))
print(solution([-1, 0, 1], [1, 0, -1]))
