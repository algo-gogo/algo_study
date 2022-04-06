# aabbcc -> 2a2b2c 같이 압축
# 출력: 가장 짧게 압축경우

def solution(s):
    if len(s) < 3:
        return len(s)

    length = len(s)
    countList = []
    for i in range(1, len(s)):
        # a
        strings = s[:i]
        count = 0
        result = ''
        for j in range(i, length // len(strings)):
            if strings == s[j:j + i]:
                count += 1
            else:
                result += strings

        countList.append(count)

    print(min(countList))

    answer = min(countList)
    return answer

print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))