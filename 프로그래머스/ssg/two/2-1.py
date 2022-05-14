from itertools import combinations
#

def check_one(one_list, two_list):
    one_count = 0
    two_count = 0
    for one in one_list:
        if one != -1:
            one_count += 1

    for two in two_list:
        if two != -1:
            two_count += 1

    if one_count < 5:
        return False
    return one_count == two_count

def check_two(one_list, two_list):
    one_correct_list = []
    two_correct_list = []
    for index, value in enumerate(one_list):
        if value != -1:
            one_correct_list.append(index)

    for index, value in enumerate(two_list):
        if value != -1:
            two_correct_list.append(index)

    return one_correct_list == two_correct_list

def check_three(one_list, two_list):
    one_score_list = []
    two_score_list = []
    for index, value in enumerate(one_list):
        if value != -1:
            one_score_list.append(value)

    for index, value in enumerate(two_list):
        if value != -1:
            two_score_list.append(value)

    return one_score_list == two_score_list


def check_student(student_dic, one, two):
    # for index, value in student_dic.items():
    #     print("one", one)
    #     print("two", two)
    one_list = student_dic[one]
    two_list = student_dic[two]
    if not check_one(one_list, two_list):
        return ("None", "None")
    if not check_two(one_list, two_list):
        return ("None", "None")
    if not check_three(one_list, two_list):
        return ("None", "None")

    return (one, two)




def solution(logs):
    answer = []

    # 수험번호, 문제번호, 받은 점수
    print(logs)

    student_dic = {}

    index_list = []


    for index, value in enumerate(logs):
        split = value.split(' ')
        student_num = split[0]
        student_dic[student_num] = [-1 for _ in range(100)]
        index_list.append(student_num)

    index_list = list(set(index_list))
    combi_list = list(combinations(index_list, 2))

    for index, value in enumerate(logs):
        split = value.split(' ')
        student_num = split[0]
        problem_num = int(split[1])
        score = int(split[2])
        student_list = student_dic[student_num]
        if student_list[problem_num] != 0:
            score = max(student_list[problem_num], score)
        student_list[int(problem_num)] = score

    print(student_dic)
    for index, value in enumerate(student_dic):
        print(value, student_dic[value])

    for index, value in enumerate(combi_list):
        one = value[0]
        two = value[1]
        student_tuple = check_student(student_dic, one, two)
        answer.append(student_tuple[0])
        answer.append(student_tuple[1])

    answer = list(set(answer))
    try:
        if len(answer) > 1:
            answer.remove("None")
    except:
        pass
    answer.sort()
    return answer

# print(solution(["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90",
#                 "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]))

# print(solution(
#     ["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100",
#      "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "1101 1 95",
#      "1101 2 100", "1101 4 100", "1101 7 100", "1101 9 100", "1102 1 95", "1102 2 100", "1102 4 100", "1102 7 100",
#      "1102 9 100"]))

# print(solution(["1901 10 50", "1909 10 50"]))
#
print(solution(
    ["0001 1 0", "0001 2 0", "0001 3 0", "0001 4 0", "0001 5 0", "0456 1 0", "0456 2 0", "0456 3 0", "0456 4 0",
     "0456 5 0"]))
