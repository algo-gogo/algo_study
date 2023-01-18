# def solution(n, left, right):
#     answer = [[0 * n] * n for _ in range(n)]
#     for i in range(len(answer)):
#         for j in range(len(answer[i])):
#             answer[i][j] = max(i, j) + 1
#
#     print(answer)
#     answer_sum = sum(answer, [])
#     print(answer_sum)
#
#     return answer_sum[left:right + 1]

def solution(n, left, right):
    answer = []
    print(answer)
    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)
    print(answer)
    return answer

print(solution(3, 2, 5))
print(solution(4, 7, 14))
