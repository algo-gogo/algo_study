### https://www.acmicpc.net/problem/1439


a = input()

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '1':
                count_to_all_zero += 1
            if string[i + 1] == '0':
                count_to_all_one += 1

    return min(count_to_all_zero, count_to_all_one)

# def find_count_to_turn_out_to_all_zero_or_all_one(string):
#     count_to_all_zero = 0
#     count_to_all_one = 0
#
#     prev_string = ''
#     for s in string:
#         if s == '1' and prev_string == '0':
#             count_to_all_zero += 1
#         prev_string = s
#
#
#     for s in string:
#         if s == '0' and prev_string == '1':
#             count_to_all_one += 1
#         prev_string = s
#
#     return min(count_to_all_zero, count_to_all_one)

# def find_count_to_turn_out_to_all_zero_or_all_one(string):
#     character = string[0:1]
#     result = 0
#     for s in string:
#         if s == character:
#             pass
#         else:
#             result += 1
#             character = s
#
#     print(result)
#     return result // 2

print(find_count_to_turn_out_to_all_zero_or_all_one(a))



# 0001100

# 반복문 돌면서 숫자가 다른 부분의 개수를 구하고 // 2 를 함