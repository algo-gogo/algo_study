from itertools import permutations

def solution(expression):
    expression = expression.replace("+", " + ") \
        .replace("-", " - ") \
        .replace("*", " * ") \
        .replace("/", " / ")
    expression_list = expression.split()
    print(expression_list)

    result_list = []
    for i in permutations(['*', '+', '-'], 3):
        expression_list_copy = expression_list[:]
        print(i)
        for j in i:
            while j in expression_list_copy:
                j_index = expression_list_copy.index(j)
                temp_value = eval(expression_list_copy[j_index - 1] + j + expression_list_copy[j_index + 1])
                expression_list_copy[j_index] = str(temp_value)
                expression_list_copy.pop(j_index - 1)
                expression_list_copy.pop(j_index)
        result_list.append(abs(int(expression_list_copy[0])))

    print(result_list)
    return max(result_list)

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))