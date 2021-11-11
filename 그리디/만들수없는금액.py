# 이코테
# N개의 동전을 이용하여 만들 수 없는 최솟값 구하기
# 3, 2, 1, 1, 9 로 만들 수 없는 최소값 -> 8

# ... 다시풀기

n = int(input())
nList = list(map(int, input().split()))

nList.sort()
print(nList)

target = 1
for i in nList:
    if target < i:
        break
    target += i

print(target)