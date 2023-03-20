# a string made of an even number of characters ("<" and/or ">") is called symmentric if all characters in its first half are "<"
# and all characters in its second half are ">".
# for example, the strings are ""(empty string), "<>", "<<>>", "<<<>>>", etc
#
# write a function solution that, given a string S consisting of N characters,
# that given a string S made of N caracters, ("<", ">" and/or "?"), returns the lenght of the longest symmetric substring
# that can be obtained after replacing question marks with "<" or ">".

# example
# S = '<><??>>' -> 4
# S = '??????' -> 6
# S = '<<?' -> 2

# def solution(S):
#     max_length = 0
#     for i in range(len(S)):
#         for j in range(i+1, len(S)+1):
#             substring = S[i:j]
#             # count the number of < and > characters in the substring
#             count_left = substring.count("<")
#             count_right = substring.count(">")
#             count_question_mark = substring.count("?")
#             # check if the substring can be made symmetric by replacing ? characters
#             if count_question_mark == abs(count_left - count_right) and (count_left + count_right + count_question_mark) % 2 == 0:
#                 # calculate the length of the symmetric substring
#                 length = min(count_left, count_right) + count_question_mark
#                 max_length = max(max_length, length)
#     return max_length

# def solution(S):
#     n = len(S)
#     max_len = 0
#
#     # loop over all possible midpoints of a symmetric substring
#     for i in range(n // 2):
#         # consider two cases: if we replace all '?' to '<', and if we replace all '?' to '>'
#         for p, q in [('>', '<'), ('<', '>')]:
#             len_left = i
#             len_right = n - i - 2
#             j = i
#             while j >= 0 and S[j] in (p, '?'):
#                 j -= 1
#                 len_left += 1
#             k = i + 1
#             while k < n and S[k] in (q, '?'):
#                 k += 1
#                 len_right += 1
#             if len_left == len_right:
#                 max_len = max(max_len, len_left * 2)
#     return max_len

def solution(S):
    left = 0
    right = 0
    question_mark = 0
    for i in S:
        if i == '<':
            if right > 0:
                left = 0
                right = 0
            left += 1
        elif i == '>':
            right += 1
        else:
            question_mark += 1

    a = (left + right + question_mark) // 2
    result = a * 2
    # if left > right:
    #     left -= right
    #     result += right * 2
    #     a = (left + question_mark) // 2
    #     result += a * 2
    # elif right > left:
    #     right -= left
    #     result += left * 2
    #     a = (right + question_mark) // 2
    #     result += a * 2
    # elif left == right:
    #     result += left * 2
    #     a = (question_mark) // 2
    #     result += a * 2
    # else:
    #     a = question_mark // 2
    #     result += a * 2

    return result


print(solution('<><??>>'))
print(solution('??????'))
print(solution('<<?'))