# 이코테
# 모두 같은 숫자가 되기 위한 최소 횟수
# 110011 00을 뒤집으면 111111이 된다.

nList = list(map(int, input()))

print(nList)

first = nList[0]
result = 1
for i in nList:
    if first != i:
        result += 1
        first = i

print(result // 2)