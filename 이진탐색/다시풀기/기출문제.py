### 정렬된 배열에서 특정 수의 개수 구하기

# n, x = map(int, input().split())
#
# n_list = list(map(int, input().split()))
# n_list.sort()
#
# print(n_list)
#
#
# def binary_search(array, start, end, target):
#     total = 0
#     middle = (start + end) // 2
#     if target == middle:
#         for i in range(middle, -1, -1):
#             if array[i] == target:
#                 total += 1
#             else:
#                 break
#         for i in range(middle + 1, len(array)):
#             if array[i] == target:
#                 total += 1
#             else:
#                 break
#         return total
#     if target < middle:
#         end = middle - 1
#         return binary_search(array, start, end, target)
#     if target > middle:
#         start = middle + 1
#         return binary_search(array, start, end, target)
#
#
# search = binary_search(n_list, n_list[0], n_list[-1], x)
# print(search)


### 고정점 찾기
#
# def binary_search(array, start, end):
#     mid = (start + end) // 2
#     if start > end:
#         return -1
#     if array[mid] == mid:
#         return mid
#     elif array[mid] < mid:
#         start = mid + 1
#         return binary_search(array, start, end)
#     elif array[mid] > mid:
#         end = mid - 1
#         return binary_search(array, start, end)
#     return -1
#
# n = int(input())
# n_list = list(map(int, input().split()))
#
# print(binary_search(n_list, 0, n - 1))


########### 공유기 설치
##### https://www.acmicpc.net/problem/2110
#
# def binary_search(array, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         current = array[0]
#         count = 1
#         for i in range(1, len(array)):
#             if array[i] >= current + mid:
#                 count += 1
#                 current = array[i]
#         if count >= c:
#             global answer
#             start = mid + 1
#             answer = mid
#         else:
#             end = mid - 1
#
# n, c = map(int, input().split())
# n_list = []
# for i in range(n):
#     a = int(input())
#     n_list.append(a)
#
# n_list.sort()
#
# start = 1
# end = n_list[-1] - n_list[0]
# answer = 0
# binary_search(n_list, start, end)
# print(answer)

# 5 3
# 1
# 2
# 8
# 4
# 9
# [1, 2, 4, 8, 9]

def binary_search(array, start, end, c):
    while start <= end:
        mid = (start + end) // 2

        # 왜 첫번째 고정??
        current = array[0]
        count = 1

        for i in range(1, len(array)):
            # mid 보다 더 짧다면 ? 설치
            if array[i] - current >= mid:
                current = array[i]
                count += 1
        # c 개보다 더 설치를 많이 할 수 있다면? mid 를 저장해놓고 mid 를 늘린다.
        if count >= c:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

n, c = map(int, input().split())
n_list = []
for i in range(n):
    a = int(input())
    n_list.append(a)

n_list.sort()

start = 1
end = n_list[-1] - n_list[0]
answer = 0

print(n_list)

binary_search(n_list, start, end, c)
print(answer)