from itertools import combinations
# def check_num(value, sentence):
#     flag = False
#     # line in line
#     print(sentence)
#     # e l o n
#     print(value)
#     real_value = list(value)
#     real_value.append(' ')
#     print(real_value)
#     for i in sentence:
#         if i in sentence:
#             flag = True
#         else:
#             flag = False
#
#     if not flag:
#         return 0
#     else:
#         return len(sentence)
#
#
# def solution(sentences, n):
#     total_alpha = []
#     for sentence in sentences:
#         alpha = []
#         alpha_score = 0
#         for i in sentence:
#             if i.isupper():
#                 alpha.append(' ')
#                 alpha_score += 1
#
#         sentence = sentence.lower()
#         for i in sentence:
#             alpha.append(i)
#         alpha_score += len(sentence)
#         alpha.append(alpha_score)
#         total_alpha.append(alpha)
#
#     print(total_alpha)
#     total = []
#     for alpha in total_alpha:
#         a = list(set(alpha))
#         total.append(a)
#     print(total)
#
#     answer = 0
#     return answer
#
#
# print(solution(["line in line", "LINE", "in lion"], 5))
# # print(solution(["ABcD", "bdbc", "a", "Line neWs"], 7))

def solution(sentences, n):
    total_alpha = []
    for sentence in sentences:
        alpha = []
        alpha_score = 0
        for i in sentence:
            if i.isupper():
                alpha.append(' ')
                alpha_score += 1

        sentence = sentence.lower()
        for i in sentence:
            alpha.append(i)
        alpha_score += len(sentence)
        alpha.append(alpha_score)
        total_alpha.append(alpha)

    print(total_alpha)
    total = []
    for alpha in total_alpha:
        a = list(set(alpha))
        total.append(a)
    print(total)


    answer = 0
    return answer


print(solution(["line in line", "LINE", "in lion"], 5))
# print(solution(["ABcD", "bdbc", "a", "Line neWs"], 7))

# from itertools import combinations
#
#
# def solution(sentences, n):
#     total_key = []
#     for sentence in sentences:
#         alpha = []
#         alpha_score = 0
#         for i in sentence:
#             if i.isupper():
#                 alpha.append(" ")
#                 alpha_score += 1
#         sentence = sentence.lower()
#         alpha_score += len(sentence)
#         for i in sentence:
#             alpha.append(i)
#         alpha = list(set(alpha))
#         alpha.append(alpha_score)
#         total_key.append(alpha)
#
#     com_list = []
#
#     for i in range(2, len(sentences) + 1):
#         com_list.extend(list(combinations(total_key, i)))
#
#     temp_list = []
#     for i in com_list:
#         for j in i:
#             temp_list += j
#         temp_list = list(set(temp_list))
#
#         key_list = []
#         count = 0
#         print(temp_list)
#         for k in temp_list:
#             if type(k) == int:
#                 count += k
#             else:
#                 key_list.append(k)
#         key_list.append(count)
#
#         total_key.append(key_list)
#
#     answer = -1
#     for i in total_key:
#         if (len(i) - 1) > n:
#             continue
#         else:
#             answer = max(answer, i[-1])
#
#     return answer
#
#
# # print(solution(["line in line", "LINE", "in lion"], 5))
# print(solution(["ABcD", "bdbc", "a", "Line neWs"], 7))
