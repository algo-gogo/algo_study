def is_right(s):
    for i in range(len(s) // 2):
        s = s.replace('()', '')
        s = s.replace('[]', '')
        s = s.replace('{}', '')
    if s == '':
        return True



# def is_right(s):
#     stack1 = []
#     stack2 = []
#     stack3 = []
#     for i in s:
#         if i == '(':
#             stack1.append(i)
#         elif i == ')':
#             if len(stack1) == 0:
#                 return False
#             else:
#                 stack1.pop()
#         if i == '[':
#             stack2.append(i)
#         elif i == ']':
#             if len(stack2) == 0:
#                 return False
#             else:
#                 stack2.pop()
#         if i == '{':
#             stack3.append(i)
#         elif i == '}':
#             if len(stack3) == 0:
#                 return False
#             else:
#                 stack3.pop()
#     if len(stack1) == 0 and len(stack2) == 0 and len(stack3) == 0:
#         return True
#     else:
#         return False


def solution(s):
    result = 0
    length = len(s)
    for i in range(length):
        new_s = s[i:] + s[0:i]
        if is_right(new_s):
            result += 1

    return result


print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))
print(solution("[{]}"))

# def solution(s):
#     count = 0
#     i = 0
#     for i in range(len(s)):
#         stack = []
#         for j in s:
#             if not stack:
#                 stack.append(j)
#                 continue
#             if stack[-1] == '[' and j == ']':
#                 stack.pop()
#             elif stack[-1] == '{' and j == '}':
#                 stack.pop()
#             elif stack[-1] == '(' and j == ')':
#                 stack.pop()
#             else:
#                 stack.append(j)
#         s = s[1:] + s[0]
#         if not stack:
#             count += 1
#     return count