# https://www.acmicpc.net/problem/14888
from itertools import permutations
import copy

n = int(input())
n_list = list(map(int, input().split()))

# + - * %
c_list = list(map(int, input().split()))

calc_list = []

for i in range(c_list[0]):
    calc_list.append("+")

for i in range(c_list[1]):
    calc_list.append("-")

for i in range(c_list[2]):
    calc_list.append("*")

for i in range(c_list[3]):
    calc_list.append("//")

print(calc_list)

per_calc_list = list(set(list(permutations(calc_list))))
print(per_calc_list)


def calc(per_calc, n_list):
    result = n_list[0]
    copy_n_list = copy.deepcopy(n_list)
    for i in range(len(copy_n_list) - 1):
        if per_calc[i] == '+':
            result = result + n_list[i + 1]
        if per_calc[i] == '-':
            result = result - n_list[i + 1]
        if per_calc[i] == '*':
            result = result * n_list[i + 1]
        if per_calc[i] == '//':
            if result < 0:
                m_result = -result // n_list[i + 1]
                result = -m_result
            else:
                result = result // n_list[i + 1]
        # if per_calc[i] == '//':
        #     if copy_n_list[i] > 0 and copy_n_list[i + 1] > 0:
        #         copy_n_list[i + 1] = eval(str(copy_n_list[i]) + per_calc[i] + str(copy_n_list[i + 1]))
        #     elif copy_n_list[i] < 0:
        #         pass
        #     else:
        #         pass
        # else:
        #     copy_n_list[i + 1] = eval(str(copy_n_list[i]) + per_calc[i] + str(copy_n_list[i + 1]))

    return result

result_list = []
for per_calc in per_calc_list:
    result_list.append(calc(per_calc, n_list))

print(result_list)
print(max(result_list))
print(min(result_list))