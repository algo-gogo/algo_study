# https://programmers.co.kr/learn/courses/30/lessons/60058

### 개수가 같으면 균형잡힌 괄호 문자열

def right_string(u):
    right_result = []
    for index, value in enumerate(u):
        right_result.append(value)
        if value == ')':
            if right_result[len(right_result) - 2] == '(':
                del right_result[len(right_result) - 1]
                del right_result[len(right_result) - 2]

    if len(right_result) == 0:
        return True
    else:
        return False


def seperate_u_v(p):
    l_count = 0
    r_count = 0
    for index, value in enumerate(p):
        if value == '(':
            l_count += 1
        elif value == ')':
            r_count += 1
        if l_count == r_count:
            u = p[:index + 1]
            v = p[index + 1:]
            return u, v

def solution(p):
    answer = ''
    if p == '':
        return answer

    # 균형잡힌 괄호 문자열 u, v로 분리
    u, v = seperate_u_v(p)
    if right_string(u):
        answer += u + solution(v)
        return answer
    else:
        answer = "(" + solution(v) + ")"
        u = u[1:]
        u = u[:-1]
        result_string = ''
        for i in u:
            if i == '(':
                result_string += ')'
            else:
                result_string += '('
        answer = answer + result_string
        return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
