
def solution(logs):
    answer = []

    logs = list(set(logs))
    person_dic = {}
    problem_dic = {}
    for log in logs:
        split = log.split(' ')
        person_dic[split[0]] = []
        problem_dic[split[1]] = 0

    for log in logs:
        split = log.split(' ')
        person_dic[split[0]].append(split[1])
        problem_dic[split[1]] += 1

    print(person_dic)
    print(problem_dic)

    print(len(person_dic) / 2)
    result_list = []
    for key, value in problem_dic.items():
        print(key, value)
        if value >= len(person_dic) / 2:
            result_list.append(key)


    result_list.sort()

    return result_list


# print(solution(
#     ["morgan string_compare", "felix string_compare", "morgan reverse", "rohan sort", "andy reverse", "morgan sqrt"]))
print(solution(["morgan sort", "felix sort", "morgan sqrt", "morgan sqrt", "rohan reverse", "rohan reverse"]))
# print(solution(["kate sqrt"]))
