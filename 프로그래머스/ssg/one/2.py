# def check_S(S):
#     try:
#         a = S[0]
#         for i in S:
#             if i != a:
#                 return False
#         return True
#     except:
#         return True
#
# def remove_S(S):
#     a = S[0]
#     for i in range(1, len(S)):
#         if S[i] != a:
#             S = S[:i - 1] + S[i + 1:]
#             return S
#         else:
#             a = S[i]
#
# def solution(S):
#
#     while not check_S(S):
#         S = remove_S(S)
#
#     return len(S)

def solution(s):
    zero_count, one_count = 0, 0
    for i in s:
        if i == '0':
            zero_count += 1
        else:
            one_count += 1

    return abs(zero_count - one_count)


print(solution("1011"))
print((solution("0110011")))
print(solution("000111"))