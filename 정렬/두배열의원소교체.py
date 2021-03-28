# 입력받는 N개의 원소를 가지고 있는 두개의 배열이 있을 때 바꿔치기 해서 A의 원소의 합이 최대가 되게 하라
# 바꿔치기 - A의 원소와B의 원소 하나를 골라 두 원소를 서로 바꾸는 것
# 배열 A의 원소의 합이 최대가 되도록 하는것
# 입력: n, k - 배열 원소의 개수 , k 는 교체 횟수
# 출력 A의 원소의 합이 최대

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))