# 입력 조건
# 첫째 줄에 테스트 케이스 T가 입력된다. (1 <= T <= 1,000)
# 매 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력된다. (1 < n, m <= 20)
# 매 테스트 케이스 둘째 줄에 n x m 위치에 매장된 금의 개수가 공백으로 구분되어 입력된다. (0 이상 100 이하의 정수)
#
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
from collections import deque
import copy

n, m = map(int, input().split())

gold_count = list(map(int, input().split()))

data = []
for i in range(0, len(gold_count), 4):
    data.append(gold_count[i:i + 4])

q = deque()

# 열
column = 0
for i in range(len(data)):
    result = data[i][column]
    q.append((i, column, result))

while q:
    row, column, result = q.popleft()
    if column + 1 == m:
        break
    if 0 <= row - 1 < n and column + 1 < m:
        value = data[row - 1][column + 1]
        q.append((row - 1, column + 1, result + value))
    if 0 <= row < n and column + 1 < m:
        value = data[row][column + 1]
        q.append((row, column + 1, result + value))
    if 0 <= row + 1 < n and column + 1 < m:
        value = data[row + 1][column + 1]
        q.append((row + 1, column + 1, result + value))

q_list = list(q)

q_list.sort(key=lambda x: x[2], reverse=True)
print(q_list[0][2])


### 답지
### 3, 4
def gold_func(n, m, data):
    copy_data = copy.deepcopy(data)
    print(copy_data)
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위
            if i - 1 >= 0:
                value = copy_data[i - 1][j - 1] + data[i][j]
                copy_data[i][j] = max(copy_data[i][j], value)
            # 왼쪽 아래
            if i + 1 < n:
                value = copy_data[i + 1][j - 1] + data[i][j]
                copy_data[i][j] = max(copy_data[i][j], value)
            # 왼쪽
            value = copy_data[i][j - 1] + data[i][j]
            copy_data[i][j] = max(copy_data[i][j], value)

    max_list = []
    print(copy_data)
    for i in range(n):
        max_list.append(max(copy_data[i]))

    print(max(max_list))


gold_func(n, m, data)
