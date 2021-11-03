n, m, k = map(int, input().split())

array = list(map(int, input().split()))
#
# array.sort()
# print(array)
# first = array[-1]
# second = array[-2]
#
# result = 0
#
# # 총 8번 최대 3번
# while m > 0:
#     for i in range(k):
#         result += first
#         m -= 1
#     result += second
#     m -= 1
#
# #####################################################################
#
# # while True:
# #     if m == 0:
# #         break
# #     for i in range(k):
# #         result += first
# #         m -= 1
# #     result += second
# #     m -=1
#
# print(result)
#
# ################################################################
#
# # first 6, second 5 일 때 (6665)를 한 묶음으로 하고 4로 안나누어 떨어지면 큰수들을 더함
#
# count = int(m / (k + 1)) * k
# count += m % (k + 1)
# result += count * first
# result += (m - count) * second
#
# print(result)

# # 5 8 3
# n, m, k = map(int, input().split())
#
# array = list(map(int, input().split()))
# array.sort()  # 1 2 3 4 5
#
# first = array[-1]
# second = array[-2]
# result = 0
#
# while m > 0:
#     for i in range(n):
#         m -= 1
#         result += first
#     result += second
#     m -= 1


array.sort(reverse=True)

print(array)

result = 0
while m > 0:
    for i in range(k):
        result += array[0]
        m -= 1
        if m == 0:
            break
    result += array[1]
    m -= 1
    if m == 0:
        break

print(result)