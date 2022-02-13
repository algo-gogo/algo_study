# deque , Counter

### deque
# 인덱싱, 슬라이싱은 사용할 수 없으나
# 삽입 삭제할 경우 빠르게 사용 가능

from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))
print(data.popleft())

# 등장 횟수를 세는 기능 제공
### Counter

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(dict(counter))