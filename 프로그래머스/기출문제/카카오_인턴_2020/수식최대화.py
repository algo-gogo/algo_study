from itertools import permutations
import copy

def solution(expression):
    answer = 0

    expression_list = []
    operation_list = []
    temp = ''
    for e in expression:
        if e.isdigit():
            temp += e
        else:
            expression_list.append(temp)
            expression_list.append(e)
            operation_list.append(e)
            temp = ''
    if temp != '':
        expression_list.append(temp)

    print(expression_list)
    operation_list = list(set(operation_list))
    print(operation_list)
    permutation_list = list(permutations(operation_list, len(operation_list)))
    print(permutation_list)

    result = []
    for permutation in permutation_list:
        copy_expression = copy.deepcopy(expression_list)
        stack = []
        for o in permutation:
            while len(copy_expression) != 0:
                e = copy_expression.pop(0)
                if e == o:
                    if o == '*':
                        stack.append(int(stack.pop()) * int(copy_expression.pop(0)))
                    elif o == '+':
                        stack.append(int(stack.pop()) + int(copy_expression.pop(0)))
                    elif o == '-':
                        stack.append(int(stack.pop()) - int(copy_expression.pop(0)))
                else:
                    stack.append(e)

    return answer


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
