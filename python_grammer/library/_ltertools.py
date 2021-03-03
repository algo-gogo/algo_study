# ****************************다시 보기
# itertools - 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리
# permutations - 모든 순열 구하기 (순열)
# combinatios - r 개의 데이터를 뽑아 순서를 고려하지 않고 나열 (조합)
# product - r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산, 원소를 중복하여 뽑음 (순열)
# combinations_with_replacement - r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합) , 중복 허용
# 주의점 - 다 객체이기 때문에 list()자료형 써서 해야한다.

from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 2))
print(result)

from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)

from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
print(result)

from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data,2))
print(result)
