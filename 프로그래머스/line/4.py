def solution(arr, brr):
    answer = 0
    for i in range(len(arr) // 2):
        if arr[i] != brr[i]:
            diff = brr[i] - arr[i]
            arr[i] += diff
            arr[i + 1] -= diff
            answer += 1
        if arr[len(arr) - i - 1] != brr[len(arr) - i - 1]:
            diff = brr[len(arr) - i - 1] - arr[len(arr) - i - 1]
            arr[len(arr) - i - 1] += diff
            arr[len(arr) - i - 2] -= diff
            answer += 1

    return answer


print(solution([3, 7, 2, 4], [4, 5, 5, 2]))
print(solution([6, 2, 2, 6], [4, 4, 4, 4]))
