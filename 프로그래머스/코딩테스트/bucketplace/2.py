import copy

def solution(call):
    global result
    length = len(call)
    value_list = []
    set_value_list = []
    for i in range(1, length + 1):
        cut_value_list = []
        for j in range(1, length + 1):
            cut_value = call[i - 1: j + i - 1].lower()
            cut_value_list.append(cut_value)
            set_value_list.append(cut_value)

        value_list.append(list(set(cut_value_list)))
    print(value_list)
    set_value_list = list(set(set_value_list))
    print(set_value_list)

    value_dic = {}
    for i in set_value_list:
        value_dic[i] = 0

    for index, value in enumerate(value_list):
        for v in value:
            value_dic[v] += 1

    print(value_dic)
    sorted_value_dic = sorted(value_dic.items(), key=lambda item: item[1], reverse=True)
    print("sorted_value_dic", sorted_value_dic)
    a = sorted_value_dic[0][1]
    result_list = []
    for key, value in sorted_value_dic:
        if a != value:
            break
        result_list.append(key)

    result_list.sort(key=lambda x: len(x), reverse=True)
    print(result_list)

    l = len(result_list[0])

    result_l = []
    for i in result_list:
        if len(i) != l:
            break
        result_l.append(i)
    print("result_l", result_l)

    copy_call = copy.deepcopy(call)

    # split_call(copy_call, result_l)

    for i in result_l:
        result = ''
        print("copy_call", copy_call)
        for c in copy_call:
            if c.lower() == i:
                copy_call = copy_call.replace(c, c.lower())
                break
        print(copy_call)
        split = copy_call.split(i)

        for j in split:
            if j == '':
                pass
            else:
                result += j

        copy_call = result

    return result


print(solution("abcabcdefabc")) # def
print(solution("abxdeydeabz"))  # xyz
print(solution("abcabca"))      # bcbc
print(solution("ABCabcA"))      # BCbc
