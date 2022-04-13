# https://programmers.co.kr/learn/courses/30/lessons/42889

def fail(stages, index):
    clear_count = 0
    not_clear_count = 0
    for i in stages:
        if i == index:
            not_clear_count += 1
        if i >= index:
            clear_count += 1
    return not_clear_count, clear_count


def solution(n, stages):
    answer = []

    stage_dic = {}

    print(stages)
    for i in range(1, n + 1):
        not_clear_count, clear_count = fail(stages, i)
        if clear_count == 0:
            stage_dic[i] = 0
        else:
            stage_dic[i] = (not_clear_count / clear_count)

    print(stage_dic)
    sorted_dict = sorted(stage_dic.items(), key=lambda item: item[1], reverse=True)
    print(sorted_dict)
    for index, value in sorted_dict:
        answer.append(index)
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
