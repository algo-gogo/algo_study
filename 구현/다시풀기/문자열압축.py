# def solution(s):
#     answer = 10000
#     for n in range(1, len(s) // 2 + 2):
#         res = ''
#         cnt = 1
#         tmp = s[:n]
#
#         for i in range(n, len(s) + n, n):
#             if tmp == s[i:i + n]:
#                 cnt += 1
#             else:
#                 if cnt == 1:
#                     res += tmp
#                 else:
#                     res += str(cnt) + tmp
#                 tmp = s[i:i + n]
#                 cnt = 1
#         # print(res)
#         answer = min(answer, len(res))
#
#     return answer

def solution(s):
    answer = 10000

    print(s)
    result_list = []
    for i in range(1, len(s) // 2 + 2):
        result = ''
        count = 1
        temp = s[:i]

        for j in range(i, len(s) + i, i):
            temp_temp = s[j:j + i]
            if temp == s[j: j + i]:
                count += 1
            else:
                if count == 1:
                    result += temp
                else:
                    result += str(count) + temp
                temp = temp_temp
                count = 1
        result_list.append(result)

    result_list.sort(key=len)
    print(result_list)

    return len(result_list[0])


print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
