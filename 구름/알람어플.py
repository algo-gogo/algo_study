from itertools import permutations
import math

# s = input()
# n = int(input())
#
# permutation_list = []
#
# for i in range(1, len(s) + 1):
#     p_list = list(permutations(s, i))
#     permutation_list.extend(p_list)
#
# permutation_list = list(set(permutation_list))
# print(permutation_list)
# permutation_list.sort()
# print(permutation_list)


s = input()
k = int(input())
length = len(s)
if length > 5000:
    print(0)
else:
    result_list = []
    for i in range(1, len(s) + 1):
        ceil = math.ceil(len(s))
        for j in range(0, ceil):
            slice = s[j: j + i]
            result_list.append(slice)

    result_list = list(set(result_list))
    result_list.sort()
    print(result_list[k - 1])
