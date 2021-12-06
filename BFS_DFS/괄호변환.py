def separation(p):
    balanceList = []
    pLeft = []
    pRight = []
    if not p:
        return '', ''
    for i in range(len(p)):
        if p[i] == "(":
            pLeft.append("(")
        else:
            pRight.append(")")
        if len(pLeft) == len(pRight):
            # 균형잡힌 문자열
            u = p[:i + 1]
            v = p[i + 1:]
            # balanceList.append(u)
            # balanceList.append(v)
            return u, v


def isBalanced(balanceString):
    rightList = []
    i = 0
    j = 0
    while i < len(balanceString):
        rightList.append(balanceString[i])
        if len(rightList) > 1:
            if rightList[j - 1] == "(" and rightList[j] == ")":
                rightList.pop(-1)
                rightList.pop(-1)
                j -= 2
        j += 1
        i += 1
    if len(rightList) == 0:
        return True
    else:
        return False

def solution(p):
    if not p:
        return ""

    result = ''
    resultList = []

    ### 균형잡힌 괄호 문자열 u, v 로 분리
    u, v = separation(p)

    result = ''

    if isBalanced(u):
        result += u + solution(v)
        return result
    else:
        emptyString = "(" + solution(v) + ")"
        u = u[1:]
        u = u[:-1]
        resultString = ''
        for i in u:
            if i == '(':
                resultString += ')'
            else:
                resultString += '('
        result = emptyString + resultString
        return result



# print(solution("(()())()"))
# print(solution(")("))
print(solution("()))((()"))
