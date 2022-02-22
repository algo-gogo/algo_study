# 합이 5인 경우의 수 찾기
n = 5
m = 5
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)


# 정렬되어 있는 두 리스트의 합집합

n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]
result = [0] * (n + m)
i = 0
j = 0
k = 0

while i < n or j < m:
    # 리스트 b의 모든 원소가 처리되었거나 리스트 a의 원소가 더 작을 때
    if j >= m or (i < n and a[i] <= b[j]):
        result[k] = a[i]
        i += 1
    else:
        result[k] = b[j]
        j += 1
    k += 1

for i in result:
    print(i, end=' ')