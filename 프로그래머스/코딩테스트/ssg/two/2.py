def check_dic(student_dic, student_num, problem_num, score):
    for index, value in enumerate(student_dic[student_num]):
        if value[0] == problem_num:
            max_score = max(int(score), int(value[1]))
            student_dic[student_num][index][1] = str(max_score)
            return student_dic

    student_dic[student_num].append([problem_num, score])

    return student_dic

def check_one(student_dic):
    for index, value in enumerate(student_dic):
        print(value, student_dic[value])

def solution(logs):
    answer = []

    # 수험번호, 문제번호, 받은 점수
    print(logs)

    student_dic = {}

    for index, value in enumerate(logs):
        split = value.split(' ')
        student_num = split[0]
        student_dic[student_num] = []

    for index, value in enumerate(logs):
        split = value.split(' ')
        student_num = split[0]
        problem_num = split[1]
        score = split[2]
        student_dic = check_dic(student_dic, student_num, problem_num, score)

    print(student_dic)

    for index, value in enumerate(student_dic):
        length = len(student_dic[value])
        student_dic[value].append(length)


    check_one(student_dic)

    return answer


print(solution(["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90",
                "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]))

# print(solution(
#     ["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100",
#      "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "1101 1 95",
#      "1101 2 100", "1101 4 100", "1101 7 100", "1101 9 100", "1102 1 95", "1102 2 100", "1102 4 100", "1102 7 100",
#      "1102 9 100"]))
#
# print(solution(["1901 10 50", "1909 10 50"]))
#
# print(solution(
#     ["0001 1 0", "0001 2 0", "0001 3 0", "0001 4 0", "0001 5 0", "0456 1 0", "0456 2 0", "0456 3 0", "0456 4 0",
#      "0456 5 0"]))
