def solution(msg):
    answer = []

    # 알파벳 딕셔너리
    dic = {chr(i + 65): i + 1 for i in range(26)}
    print(dic)

    i_setting = 0
    for i in range(len(msg)):
        if i < i_setting:
            continue
        for j in range(len(msg), i - 1, -1):
            if msg[i:j] in dic:
                answer.append(dic[msg[i:j]])
                dic[msg[i:j + 1]] = len(dic) + 1
                i_setting = j
                break

    return answer


print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))
