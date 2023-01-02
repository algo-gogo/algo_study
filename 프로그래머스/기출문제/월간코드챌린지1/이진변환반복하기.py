def solution(s):
    answer = []

    count = 0
    zero_count = 0
    while s != 1:
        for i in s:
            if i == '0':
                zero_count += 1
        s = s.replace('0', '')
        count += 1
        if len(s) == 1:
            break

        s = bin(len(s))[2:]
        s = str(s)


    answer.append(count)
    answer.append(zero_count)
    return answer


print(solution("110010101001"))
# print(solution("01110"))
# print(solution("1111111"))