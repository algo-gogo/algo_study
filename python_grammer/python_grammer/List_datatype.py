# 리스트 인덱싱
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(array[-1])

# 리스트의 슬라이싱 - 두번째 부터 4 번째
print(array[1: 4])

# 리스트 초기화
n = 10
a = [0] * n
print(a)

# 리스트 컴프리헨션   *********************************
array2 = [i for i in range(20)]
# 짝수 표현
array2 = [i for i in range(20) if i % 2 == 0]
print(array2)

# 1 부터 9 까지의 제곱 값을 포함하는 리스트
array2 = [i * i for i in range(1, 10)]
print(array2)

# N * M 크기의 2차원 리스트 초기화
n = 3
m = 4
array3 = [[0] * m for _ in range(n)]
print(array3)

# remove_set 에 포함되지 않은 값만을 저장
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# 2차원 리스트를 초기화할 떄는 반드시 컴프리헨션을 이용해야함 *******************

result = [i for i in a if i not in remove_set]
print(result)

# X in list
# X not in 문자열

# 리스트 관련 메서드들
array4 = [1, 2, 3, 4, 5, 6, 7]
array4.append(3)
array4.sort()
array4.sort(reverse=True)
array4.reverse()
array4.insert(2, 4)  # 인덱스 / 값
array4.count()
array4.remove(2)


