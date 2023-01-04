def quad(a, b, l, arr, result):
    start = arr[a][b]
    for i in range(a, a + l):
        for j in range(b, b + l):
            if start != arr[i][j]:
                l = l // 2
                quad(a, b, l, arr, result)
                quad(a, b + l, l, arr, result)
                quad(a + l, b, l, arr, result)
                quad(a + l, b + l, l, arr, result)
                return
    result[start] += 1


def solution(arr):
    result = [0, 0]
    length = len(arr)

    quad(0, 0, length, arr, result)

    return result


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 1]]))
