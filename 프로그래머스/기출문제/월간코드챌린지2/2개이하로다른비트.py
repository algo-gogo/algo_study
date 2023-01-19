def solution(numbers):
    answer = []

    for n in numbers:
        if n % 2 == 0:
            answer.append(n + 1)
        else:
            binary = bin(n)[2:]
            while True:
                n += 1
                if bin(n)[2:].count('1') >= binary.count('1'):
                    answer.append(n)
                    break

    return answer


print(solution([2, 7]))
