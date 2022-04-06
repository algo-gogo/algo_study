def solution(s):
    answer = 10000
    for n in range(1, len(s) // 2 + 2):
        res = ''
        cnt = 1
        tmp = s[:n]

        for i in range(n, len(s) + n, n):
            if tmp == s[i:i + n]:
                cnt += 1
            else:
                if cnt == 1:
                    res += tmp
                else:
                    res += str(cnt) + tmp
                tmp = s[i:i + n]
                cnt = 1
        # print(res)
        answer = min(answer, len(res))

    return answer


print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
