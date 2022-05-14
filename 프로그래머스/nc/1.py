# import copy
#
# def solution(movie):
#     answer = []
#
#     copy_movie = copy.deepcopy(movie)
#     movie_dic = {}
#
#     move_set_list = list(set(copy_movie))
#     for i in move_set_list:
#         movie_dic[i] = 0
#
#     for m in movie:
#         movie_dic[m] += 1
#
#     print(movie_dic)
#     sorted_dict = sorted(movie_dic.items(), key = lambda item: item[1], reverse = True)
#     print(sorted_dict)
#
#     for i in sorted_dict:
#         answer.append(i[0])
#
#     return answer

from collections import Counter

def solution(movie):
    answer = []
    movie_counter = dict(Counter(movie))
    print(movie_counter)
    sorted_dict = sorted(movie_counter.items(), key=lambda item: item[1], reverse=True)
    sorted_dict.sort(key=lambda x:(-x[1], x[0]))
    for i in sorted_dict:
        answer.append(i[0])

    return answer


print(solution(["spy", "ray", "spy", "room", "once", "ray", "spy", "once"]))


