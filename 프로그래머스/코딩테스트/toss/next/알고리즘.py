### 1

# 팬디지털을 만족하는 solution을 작성하라
# 팬디지털이란 길이가 N인 substring을 10진수로 읽은 숫자
# 1부터 N까지의 숫자를 하나씩 사용하여 만든 N자리 숫자입니다.
# def solution(s, N):
#     answer = 0
#
#     # 1. s를 N개씩 자른다.
#     # 2. 자른 것을 10진수로 읽는다.
#     # 3. 1부터 N까지의 숫자를 하나씩 사용하여 만든 N자리 숫자를 팬디지털이라고 한다.
#     # 4. 팬디지털 중 가장 큰 수를 리턴한다.
#     for i in range(len(s) - N + 1):
#         temp = s[i:i+N]
#         temp = int(temp)
#         n_list = [str(i) for i in range(1, N + 1)]
#         if temp > answer:
#             a = list(str(temp))
#             a.sort()
#             if a == n_list:
#                 answer = temp
#     if answer == 0:
#         return -1
#
#     return answer
#
# print(solution("1451232125", 2)) # 21