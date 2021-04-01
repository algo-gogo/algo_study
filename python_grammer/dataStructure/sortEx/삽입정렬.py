# 삽입 정렬은 특정한 데이터를 적절한 위치에 '삽입'한다는 의미에서 삽입정렬 이라고 부른다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

# 시간 복잡도 - 반복문이 2번 충첩되어 사용되었지만
# 데이터가 어느정도 정렬 되어 있다면 빠르게 동작함

####################################################
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

# 예제) 7 1 9 2 6 3 5 0 4 8
# ->   1 7 9 2 6 3 5 0 4 8
# ->   1 7 9 2 6 3 5 0 4 8
# ->   1 2 7 9 6 3 5 0 4 8 ....

# for i in range(len(array)):
#     for j in range(i, 0, -1):
#         if array[j] < array[j-1]:
#             array[j], array[j-1] = array[j-1], array[j]
#         else:
#             break
