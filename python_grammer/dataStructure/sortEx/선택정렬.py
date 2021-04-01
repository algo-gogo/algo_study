# 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고,
# # 그 다음 작은 데이터를 선택해 앞에서 두번째 데이터와 바꾸는 과정 반복
#
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
#
# for i in range(len(array)):
#     min_index = i
#     for j in range(i + 1, len(array)):
#         if array[min_index] > array[j]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i]  # 스왑 코드
#
# print(array)
#
# # 시간 복잡도 - O(n^2) -- 데이터 개수가 늘어 날 수록 엄청 커짐

##############################################

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_value = i
    for j in range(i + 1, len(array)):
        if array[min_value] > array[j]:
            min_value = j
        array[i], array[min_value] = array[min_value], array[i]

print(array)
