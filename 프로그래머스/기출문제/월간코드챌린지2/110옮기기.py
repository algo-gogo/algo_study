import copy

def solution(s):
    answer = []

    for i in s:
        print(i)
        s_list = []
        replace = i.replace('110', '')
        r_list = list(replace)
        print(r_list)
        for j in range(len(r_list) + 1):
            copy_r = copy.deepcopy(r_list)
            copy_r.insert(j, '110')
            s_list.append(''.join(copy_r))
        s_list.sort()
        print("sdf", s_list)
        answer.append(s_list[0])

    return answer


print(solution(["1110", "100111100", "0111111010"]))
