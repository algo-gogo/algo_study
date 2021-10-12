# 이코테
# 02984  각 자리수들을 더하기(+) 곱하기(*) 해서 최댓값 구하기

nList = list(map(int, input()))

result = 1
for i in nList:
    if i == 0:
        pass
    else:
        result *= i
print(result)