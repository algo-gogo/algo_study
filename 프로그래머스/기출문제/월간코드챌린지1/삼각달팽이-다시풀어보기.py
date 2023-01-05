def solution(n):
    answer = []

    for i in range(n):
        answer.append([0] * (i + 1))

    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1

    return sum(answer, [])


print(solution(4))
print(solution(5))
print(solution(6))
