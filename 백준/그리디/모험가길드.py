# 공포도가 x 인 모험가는 x명 이상이 그룹으로
# 입력: n, n개의 공포도
# 출력: 최대 몇개의 그룹인가?
# 입력: 5
#      2 3 1 2 2
#
n = int(input())

nList = list(map(int, input().split()))
nList.sort()

# 1 2 2 2 3
print(nList)

result = 0

# 인원수
count = 0
for i in nList:
    count += 1
    if i == count:
        result += 1
        count = 0

print(result)
