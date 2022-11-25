def solution(s):
    # 3
    r_list = ['111', '222', '333', '444', '555', '666', '777', '888', '999']
    result_list = []
    for i in range(len(s) - 2):
        a = s[i:i + 3]
        if a in r_list:
            result_list.append(int(a))

    if len(result_list) == 0:
        return -1
    else:
        return max(result_list)


print(solution("12223"))
print(solution("111999333"))
print(solution("123"))
