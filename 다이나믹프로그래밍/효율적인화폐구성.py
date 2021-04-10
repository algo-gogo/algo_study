# 요약
# N 가지의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록
# 입력: n(화폐의 종류) m(만들고자 하는 값) , n개의 화폐의 가치
# 출력: m을 만드는데 최소의 개수, 만약 만들 수 없다면 -1
n, m = map(int, input())  # 2, 15

array = []  # 2 3
for i in range(n):
    array.append(int(input()))

d = [10001] * m + 1
d[0] = 0

for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 1001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
