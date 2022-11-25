# https://www.acmicpc.net/problem/1541

# def solution(s):
#
#     s = input()
#     split = s.split('-')
#
#     split_sum = 0
#     for i in range(1, len(split)):
#         split_sum += sum(map(int, split[i].split('+')))
#
#     f_split = sum(map(int, split[0].split('+')))
#
#     return f_split - split_sum
#
#
# print(solution("55-50+40"))
# print(solution("10+20+30+40"))
# print(solution("00009-00009"))

s = input()
split = s.split('-')

split_sum = 0
for i in range(1, len(split)):
    split_sum += sum(map(int, split[i].split('+')))

f_split = sum(map(int, split[0].split('+')))

print(f_split - split_sum)