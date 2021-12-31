# https://www.acmicpc.net/problem/1463
# 요약
# 정수 X가 주어질 때
# 1. X가 5로 나누어 떨어지면 5로 나눈다
# 2. X가 3으로 나누어 떨어지면 3으로 나눈다
# 3. X가 2로 나누어 떨어지면 2로 나눈다
# 4. X에서 1을 뺀다
# 1을 만들려고하는데 연산을 사용하는 횟수의 최솟값을 출력

# n = int(input())
#
# d = [0] * 30001
#
# for i in range(2, n + 1):
#     d[i] = d[i - 1] + 1
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i // 5] + 1)
#
# print(d[n])
#####################################

n = int(input())

d = [0] * (n + 1)

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

print(d[n])