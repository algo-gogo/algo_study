def solution(registered_list, new_id):
    if new_id not in registered_list:
        return new_id
    else:
        split_index = len(new_id)
        for i in range(len(new_id)):
            if new_id[i].isnumeric():
                split_index = i
                break
        S = new_id[:split_index]
        N = new_id[split_index:]
        if N == '':
            n = 0
        else:
            n = int(N)
        n1 = str(n + 1)
        new_id_1 = S + n1
        return solution(registered_list, new_id_1)

# def solution(registered_list, new_id):
#     if new_id not in registered_list:
#         return new_id
#     else:
#         split_index = len(new_id)
#         for i in range(len(new_id)):
#             if new_id[i].isdigit():
#                 split_index = i
#                 break
#         if split_index == len(new_id):
#             return new_id + "1"
#         else:
#             new_id = new_id[:split_index]
#             number = int(new_id[split_index:])
#             while new_id + str(number) in registered_list:
#                 number += 1
#             return new_id + str(number)


print(solution(["card", "ace13", "ace16", "banker", "ace17", "ace14"], "ace15"))
print(solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow"))
