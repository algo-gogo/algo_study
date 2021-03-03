data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'coconut'

key_list = data.keys()

value_list = data.values()

for i in data:
    print(i)

# 집합 자료형 - 중복 허용X, 순서가 없음
# 집합 자료형 초기화 방법
data = set([1, 1, 2, 3, 4])
data = {1, 2, 3, 4, 5, 1}

data.add(4)
data.update([2, 6])
data.remove(3)
