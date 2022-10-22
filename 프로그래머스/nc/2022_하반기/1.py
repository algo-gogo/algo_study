import copy

# def solution(source):
#
#     alpha_list = []
#     if source == "":
#         return source
#
#     new_source = copy.deepcopy(source)
#     new_source_list = list(new_source)
#
#     for char in source:
#         if char in alpha_list:
#             continue
#         else:
#             new_source_list.remove(char)
#             alpha_list.append(char)
#
#     new_source_join = "".join(new_source_list)
#     print(new_source_join)
#     alpha_list.sort()
#     join = "".join(alpha_list)
#     print(join)
#
#     return join + new_source_join

def solution(source):

    alpha_list = []
    dest = ""
    if source == "":
        return source

    new_source = copy.deepcopy(source)
    new_source_list = list(new_source)

    for char in source:
        if char in alpha_list:
            continue
        else:
            new_source_list.remove(char)
            alpha_list.append(char)

    new_source_join = "".join(new_source_list)
    alpha_list.sort()
    print(alpha_list)
    join = "".join(alpha_list)
    print(dest)

    return join + solution(new_source_join)

print(solution("execute"))
print(solution("cucumber"))
print(solution("bbaadb"))

