# 시간 초과
def solution(X, Y):
    x_list = list(X)
    y_list = list(Y)
    result_list = []
    x_length = len(x_list)
    y_length = len(y_list)
    if x_length >= y_length:
        for y in y_list:
            if y in x_list:
                result_list.append(y)
                x_list.remove(y)
    else:
        for x in x_list:
            if x in y_list:
                result_list.append(x)
                y_list.remove(x)

    if len(result_list) == 0:
        return "-1"
    else:
        s = list(set(result_list))
        print(s)
        if len(s) == 1 and s[0] == '0':
            return "0"
        else:
            result_list.sort(reverse=True)
            join = ''.join(result_list)
            return join


print(solution("100", "2345"))
print(solution("100", "203045"))
print(solution("100", "123450"))
print(solution("12321", "42531"))
print(solution("5525", "42531"))
