def remove_same(answer_list):
    result = []
    for i in answer_list:
        a = []
        for j in i:
            if j not in a:
                a.append(j)
        result.append(a)
    return result

def find_short(answer_list, real_answer_list):
    answer = []
    answer_list.sort(key=len)

    print(answer_list)
    if len(answer_list) == 0:
        answer_list.append('None')
    short_length = len(answer_list[0])
    for i in answer_list:
        if len(i) == short_length:
            answer.append(i)
        else:
            break
    answer.sort()
    real_answer_list.append(answer)


def find_search(value, target):
    count = 0
    for i in value:
        if i.find(target) != -1:
            count += 1

    if count == 1:
        return target


def solution(goods):
    answer_list = []
    for index, value in enumerate(goods):
        length = len(value)
        answer_list_list = []
        for j in range(1, length + 1):
            for k in range(1, length + 1):
                cut_value = value[j - 1:k + j - 1]
                search = find_search(goods, cut_value)
                if search is not None:
                    answer_list_list.append(search)
        answer_list.append(answer_list_list)

    real_answer_list = []
    for i in answer_list:
        find_short(i, real_answer_list)
    print(real_answer_list)
    result = remove_same(real_answer_list)

    answer = []
    for i in result:
        answer_value = ''
        length = len(i)
        for j in range(len(i)):
            value = i[j]
            if j == length - 1:
                answer_value = answer_value + value
            else:
                answer_value = answer_value + value + ' '

        answer.append(answer_value)

    return answer


# print(solution(["pencil", "cilicon", "contrabase", "picturelist"]))
print(solution(["abcdeabcd","cdabe","abce","bcdeab"]))
