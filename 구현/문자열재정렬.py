# 앏파벳 대문자와 숫자로만 구성된 문자열
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한뒤 그 모든 숫자들을 더하라
# 입력: K1KA5CB7
# 출력: ABCKK13

n = list(input())

n.sort()

numList = []
result = ''
for i in n:
    if ord(i) >= 65:
        result += i
    else:
        numList.append(i)

numResult = 0
for i in numList:
    numResult += int(i)

result += str(numResult)

print(result)

