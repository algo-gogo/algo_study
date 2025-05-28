# (, ) 의 개수가 맞을 경우 => 균형잡힌 괄호 문자열
# (, ) 개수, 짝도 맞을 경우 => 올바른 괄호 문자열
# 균형잡힌 문자열 => 올바른 문자열로 변환 가능
# 균형잡힌 문자열을 올바른 문자열로 변환하라

def right_string(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                return False
    if not stack:
        return True
    else:
        return False

def solution(p):
    answer = ''

    # 1. 입력이 빈 문자열 => 빈 문자열 반환
    if p == '':
        return ''
    # 2. w를 두 균형잡힌 문자열 u, v로 분리
    u = ''
    v = ''
    left_count = 0
    right_count = 0
    for i in range(len(p)):
        if p[i] == '(':
            left_count += 1
        elif p[i] == ')':
            right_count += 1
        if left_count == right_count:
            u = p[:i + 1]
            v = p[i + 1:]
            break

    # 3. u가 올바른 문자열 => v도 위 과정 반복
    if right_string(u):
        answer += u + solution(v)
        return answer
    # 4. 문자열 u가 올바른 문자열이 아니라면
    else:
        answer = '(' + solution(v) + ')'
        for i in u[1:-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer
    # 4-1. 빈 문자열에 첫번째 문자로 (추가
    # 4-2. v에 대해 1단계부터 재귀적으로 수행한것을 이어붙임
    # 4-3. ) 를 붙임
    # 4-4. u의 첫, 마지막 제거, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임
    # 4-5. 생성된 문자 반환

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))