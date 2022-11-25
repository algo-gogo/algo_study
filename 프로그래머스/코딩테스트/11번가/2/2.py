
MAX_VALUE = 100000000
def solution(A):
    non_empty_list = []
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            breakPoint = 0
            value = abs(A[i] - A[j])
            value2 = min(A[i], A[j])
            if value in [0, 1]:
                non_empty_list.append(value)
            for k in range(1, value):
                if value2 + k in A:
                    breakPoint = -1
                    break
            if breakPoint != -1:
                non_empty_list.append(value)

    print(non_empty_list)
    if len(non_empty_list) == 0:
        return -2

    min_value = min(non_empty_list)
    if min_value > MAX_VALUE:
        return -1
    return min_value

print(solution([0, 3, 3, 7, 5, 3, 11, 1]))