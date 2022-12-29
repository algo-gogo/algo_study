def solution(cookie):
    answer = 0

    for i in range(len(cookie) - 1):
        left = cookie[i]
        right = cookie[i + 1]
        left_index = i
        right_index = i + 1

        while True:
            if left == right:
                answer = max(answer, left)
            if left <= right:
                left_index -= 1
                if left_index < 0:
                    break
                left += cookie[left_index]
            else:
                right_index += 1
                if right_index >= len(cookie):
                    break
                right += cookie[right_index]

    return answer


print(solution([1, 1, 2, 3]))
print(solution([1, 2, 4, 5]))
