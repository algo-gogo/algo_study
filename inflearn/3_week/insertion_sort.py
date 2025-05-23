input = [4, 6, 2, 9, 1]


# 4, 6 비교

# 4, 6, 2 => 4, 2, 6 => 2, 4, 6

def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i):
            if array[i - j] < array[i - j - 1]:
                array[i - j], array[i - j - 1] = array[i - j - 1], array[i - j]
            else:
                break

    return array

# def insertion_sort(array):
#     for i in range(len(array) - 1):
#         for j in range(i + 1, 0, -1):
#             if array[j - 1] > array[j]:
#                 array[j - 1], array[j] = array[j], array[j - 1]
#             else:
#                 break
#
#     print(array)
#     return array


insertion_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ", insertion_sort([5, 8, 4, 7, 7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ", insertion_sort([3, -1, 17, 9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ", insertion_sort([100, 56, -3, 32, 44]))
