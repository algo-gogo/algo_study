# 이진 탐색을 쉽게 구현할 수 있도록 bisect라이브러리 제공
# 정렬된 배열에서 특정한 원소를 찾을 때

# bisect_left() - 정렬을 유지하면서 리스트 a에 데이터 x 를 삽일할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right() - 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

# 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구할 때 효과적

# 시간복잡도 O(lonN)

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]

x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))


################################## 이거 유심히 볼것!!~~!!!!!!!~~~~~~~~~~~~~~~~~~~~~~~
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


array = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수
print(count_by_range(a, -1, 3))

