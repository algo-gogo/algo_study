# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def is_correct_parenthesis(string):
    string_list = list(string)
    stack = []
    for ss in string_list:
        if ss == '(':
            stack.append(ss)
        elif ss == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                return False

    if len(stack) > 0:
        return False

    return True


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))
