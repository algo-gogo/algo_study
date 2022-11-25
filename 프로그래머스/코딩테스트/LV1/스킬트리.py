import copy


def solution(skill, skill_trees):
    result_list = []
    for skill_tree in skill_trees:
        skill_copy = copy.deepcopy(skill)
        result = []
        for i in range(len(skill_copy)):
            s = skill[i]
            if s in skill_tree:
                result.append(skill_tree.index(s))
            else:
                result.append(1000000000)
        result_list.append(result)

    print(result_list)

    answer = 0
    for result in result_list:
        if sorted(result) == result:
            answer += 1

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
# print(solution("CBD", ["BACDE", "CBADF", "AEC", "BDA"]))

# def solution(skill, skill_trees):
#     answer = 0
#     new_skill_trees = []
#     for i in skill_trees:
#         temp = ""
#         for j in i:
#             if j in skill:
#                 temp += j
#         new_skill_trees.append(temp)
#
#     for i in new_skill_trees:
#         if len(i) <= 1:
#             answer += 1
#             continue
#         flag = True
#         for j in range(len(i) - 1):
#             if skill.index(i[j]) > 0:
#                 for x in range(skill.index(i[j])):
#                     if skill[x] not in i:
#                         flag = False
#             if skill.index(i[j]) - skill.index(i[j + 1]) > 0:
#                 flag = False
#         if flag:
#             answer += 1
#
#     return answer
#
# print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
# print(solution("CBD", ["BACDE", "CBADF", "AEC", "BDA"]))

# def solution(skill, skill_trees):
#     skill = list(skill)
#     print(skill)
#
#     result_list = []
#     for skill_tree in skill_trees:
#         result = []
#         # C B D
#         skill_copy = copy.deepcopy(skill)
#         skill_tree_list = list(skill_tree)
#
#         for sc in skill_copy:
#             if sc in skill_tree_list:
#                 result.append(skill_tree_list.index(sc))
#             else:
#                 result.append(-1)
#         result_list.append(result)
#
#     print(result_list)
#
#     answer = 0
#     for result in result_list:
#         if -1 in result:
#             if result.index(-1) != 2:
#                 continue
#             else:
#                 result.pop(-1)
#                 if sorted(result) == result:
#                     answer += 1
#         elif sorted(result) == result:
#             answer += 1
#
#     return answer
#
# print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
# print(solution("CBD", ["ABCD", "CBDA", "DB", "BDA"]))
