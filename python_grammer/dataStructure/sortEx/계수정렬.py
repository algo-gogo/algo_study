# 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘이다.
# 기수정렬과 더불어 가장 빠름      ... 기수정렬도 볼것...
# 별도의 리스트를 선언하고 그에 맞는 인덱스에 넣는다.
# 가장 큰데이터와 가장 작은 데이터의 차이가 너무 크다면 사용X
# -> 모든 범위를 담을 수 있는 크기의 리스트를 선언해야하기 때문이다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
