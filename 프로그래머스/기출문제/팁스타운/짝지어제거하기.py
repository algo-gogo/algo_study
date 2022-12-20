# def solution(s):
#     prev_word = ''
#     while s != '':
#         num = 0
#         s_num = len(s)
#         for i in s:
#             num += 1
#             if i == prev_word:
#                 s = s.replace(i * 2, '')
#                 break
#             prev_word = i
#         if s_num == len(s):
#             return 0
#         if s == '':
#             return 1

def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])

    if stack:
        return 0
    else:
        return 1


print(solution('baabaa'))
print(solution('cdcd'))