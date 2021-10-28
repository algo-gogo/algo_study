# 이테코
# 입력
# 첫째줄: 볼링공의 개수 N, 공의 최대 무게 M
# 둘째줄: 각 볼링공의 무게 K
# 출력조건: 두 사람이 볼링공을 고르는 경우의 수

n, m = map(int, input().split())
k = list(map(int, input().split()))

list = []
countList = [0 for i in range(m+1)]
print(countList)

for i in range(len(k)):
    countList[k[i]] += 1

print(countList)

# count = 0
# for i in (0, 3):
#     for j in (i+1, 5):
#         count += countList[i] * countList[j]
#
# print(count)

count = 0
for i in range(1, 4):
    n -= countList[i]
    count += countList[i] * n

print(count)


# 인터넷 검색
# count = 0
# for i in range(1, m+1):
#     n -= countList[i]
#     count += countList[i] * n
#
# print(count)