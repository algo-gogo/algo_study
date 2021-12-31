# 요약
# 서로 인접한 식량창고를 건들 순 없다 -> 최소한 한칸 이상은 떨어져 있어야한다.
# N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값

n = int(input())

array = list(map(int, input().split()))
d = [0] * n

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n - 1])

