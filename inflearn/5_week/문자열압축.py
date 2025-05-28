def solution(string):

    # a a b b a c c c
    # 2a 2b a c c c
    # a a b b a 3c
    result_list = []
    for i in range(1, len(string) // 2 + 2):
        result = ''
        count = 1
        temp = string[:i] # a
        for j in range(i, len(string) + i, i):
            temp_temp = string[j:j + i]
            if temp == temp_temp:
                count += 1
            else:
                if count == 1:
                    result += temp
                else:
                    result += str(count) + temp
                    count = 1
                temp = temp_temp
        result_list.append(result)

    result_list.sort(key=lambda x: len(x))
    print(result_list)
    return len(result_list[0])

print("정답 = 7 / 현재 풀이 값 = ", solution("aabbaccc"))
print("정답 = 9 / 현재 풀이 값 = ", solution("ababcdcdababcdcd"))
print("정답 = 8 / 현재 풀이 값 = ", solution("abcabcdede"))
print("정답 = 14 / 현재 풀이 값 = ", solution("abcabcabcabcdededededede"))
print("정답 = 17 / 현재 풀이 값 = ", solution("xababcdcdababcdcd"))
