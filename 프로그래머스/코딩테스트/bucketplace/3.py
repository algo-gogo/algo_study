import copy


def solution(tstring, var):
    var_dic = {}
    for i in range(len(var)):
        var_dic[var[i][0]] = var[i][1]

    print(var_dic)
    count = 0

    copy_string = copy.deepcopy(tstring)

    cycle_list = []
    for i in var_dic:
        cycle_list.append(i)

    print(cycle_list)
    is_cycle = False
    if len(cycle_list) >= 2:
        for i in range(len(cycle_list)):
            try:
                i = i
                i_ = var_dic[cycle_list[i]]
                i__ = cycle_list[i]
                i__replace = i_.replace("{", "")
                replace_replace = i__replace.replace("}", "")
                if var_dic[replace_replace] == "{" + cycle_list[i] + "}":
                    is_cycle = True
            except:
                continue

    print(is_cycle)

    if is_cycle:
        return copy_string
    else:
        while count < len(var_dic) ** len(var_dic):
            for i in var_dic:
                replace = copy_string.replace("{" + i + "}", var_dic[i])
                copy_string = replace

            count += 1

    return copy_string


# print(solution("this is {template} {template} is {state}",
#                [["template", "string"], ["state", "changed"]]))
#
# print(solution("this is {template} {template} is {state}",
#                [["template", "string"], ["state", "{template}"]]))

# print(solution("this is {template} {template} is {state}",
#                [["template", "{state}"], ["state", "{template}"]]))

print(solution("{a} {b} {c} {d} {i}",
               [["b", "{c}"], ["a", "{b}"], ["e", "{f}"], ["h", "i"], ["d", "{e}"], ["f", "{d}"], ["c", "d"]]))
