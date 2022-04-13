# https://www.acmicpc.net/problem/1715

# n = int(input())
# n_list = []
# for i in range(n):
#     a = int(input())
#     n_list.append(a)
#
# n_list.sort()
#
# result = 0
# for i in range(1, len(n_list)):
#     value = n_list[i]
#     result += n_list[i] + n_list[i - 1]
#     n_list[i] = result
#
# print(n_list[-1])

##########################3
import heapq

n = int(input())
n_list = []
for i in range(n):
    a = int(input())
    heapq.heappush(n_list, a)

print(n_list)

result = 0
for i in range(1, len(n_list)):
    first = heapq.heappop(n_list)
    second = heapq.heappop(n_list)
    sum_n = first + second
    result += sum_n
    heapq.heappush(n_list, sum_n)

print(result)