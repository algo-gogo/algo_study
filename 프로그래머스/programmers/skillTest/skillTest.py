def solution(s):
    # for i in s:
    #     if not i.isnumeric():
    #         return False
    # return True
    if len(s) == 4 or len(s) == 6:
        return s.isnumeric()
    return False

print(solution("1a34"))

# a, b = map(int, input().strip().split(' '))
# print(a + b)
# for i in range(b):
#     for j in range(a):
#         print("*", end='')
#     print()

