def solution(n, a, b):
    answer = 0

    while True:
        answer += 1
        if a % 2 == 0:
            a = a // 2
        else:
            a = a // 2 + 1
        if b % 2 == 0:
            b = b // 2
        else:
            b = b // 2 + 1
        if a == b:
            break

    return answer + 1


print(solution(8, 4, 7))
