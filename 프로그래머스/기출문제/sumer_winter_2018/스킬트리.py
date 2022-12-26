# def solution(skill, skill_trees):
#
#     answer = 0
#     result_list = []
#     for skill_tree in skill_trees:
#         a = []
#         for i in range(len(skill)):
#             s = skill[i]
#             if s in skill_tree:
#                 a.append(skill_tree.index(s))
#             else:
#                 a.append(1e9)
#         result_list.append(a)
#
#     print(result_list)
#
#     for result in result_list:
#         if result == sorted(result):
#             answer += 1
#
#     return answer

def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer

print(solution('CBD', ['BACDE', 'CBADF', 'AECB', 'BDA']))