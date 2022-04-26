#################################### 부품 찾기

# 5
# 8 3 7 9 2
# 3
# 5 7 9

# def binary_search(array, start, end, target):
#     while start <= end:
#         middle = (start + end) // 2
#         if array[middle] == target:
#             return True
#         if array[middle] > target:
#             end = middle - 1
#         if array[middle] < target:
#             start = middle + 1
#     return False
#
#
# n = int(input())
# n_list = list(map(int, input().split()))
#
# m = int(input())
# m_list = list(map(int, input().split()))
#
# n_list.sort()
#
# print(n_list)
# print(m_list)
# for m in m_list:
#     if binary_search(n_list, 0, len(n_list) - 1, m):
#         print("yes", end=' ')
#     else:
#         print("no", end=' ')


#################################### 떡볶이 떡 만들기

# 4 6
# 19 15 10 17
# target 은 자른 떡의 길이
def binary_search(array, start, end, target):
    while start <= end:
        middle = (start + end) // 2
        length = 0
        for i in array:
            if i - array[middle] > 0:
                length += i - array[middle]
        if length == target:
            return array[middle]
        if length < target:
            start = middle + 1
        if length > target:
            end = middle - 1


n, m = map(int, input().split())
n_list = list(map(int, input().split()))

n_list.sort()
print(binary_search(n_list, 0, len(n_list) - 1, m))
