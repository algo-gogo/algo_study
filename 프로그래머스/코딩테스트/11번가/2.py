def check_bulb(result, index):
    for i in range(index, -1 , -1):
        if result[i] == 0:
            return 0
    return 1


def solution(A):
    result = [0 for _ in range(len(A))]

    count = 0
    for index, value in enumerate(A):
        result[value - 1] = 1
        count += check_bulb(result, value - 1)

    return count

### 전구 문제
# 이전 전구가 다 켜져 있어야지 스위치가 켜짐

print(solution([2, 3, 4, 1, 5]))
print(solution([1, 3, 4, 2, 5]))
