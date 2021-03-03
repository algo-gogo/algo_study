# 가장 많이 사용   - 병합 정렬도 볼것
# 기준을 설정(피벗)한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식
# 책보는 것이 이해하기 빠름...

# array = [7,5,9,0,3,1,6,2,4,8]

# def quick_sort(array, start, end):
#   if start >=end:
#     return
#   pivot = start
#   left = start+1
#   right = end
#   while left <= right:
#     #피벗보다 큰 데이터 찾을 때까지 반복
#     while left <= end and array[left] <= array[pivot]:
#       left +=1
#     # 피벗보다 작은 데이터를 찾을 때까지 반복
#     while right > start and array[right] >= array[pivot]:
#       right -= 1
#     if left > right:
#       array[right], array[pivot] = array[pivot], array[right]
#     else:
#       array[left], array[right] = array[right], array[left]

#   quick_sort(array, start, right -1)
#   quick_sort(array, right+1, end)

# quick_sort(array, 0, len(array)-1)
# print(array)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
