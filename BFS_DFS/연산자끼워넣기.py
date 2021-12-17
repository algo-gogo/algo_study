from itertools import permutations
from itertools import combinations


n = int(input())

numList = list(map(int, input().split()))

# 더하기, 빼기, 곱하기, 나누기
plus, minus, mul, divide = map(int, input().split())
operator = ['+', '-', '*', '//']


print(numList)


def addOperation():
    operatorList = []
    for i in range(plus):
        operatorList.append('+')

    for i in range(minus):
        operatorList.append('-')

    for i in range(mul):
        operatorList.append('*')

    for i in range(divide):
        operatorList.append('//')
    return operatorList


operationList = addOperation()
selectOperation = list(permutations(operationList, len(operationList)))
print(selectOperation)

length = len(operationList)

resultList = []

for i in range(len(selectOperation)):
    result = numList[0]
    for j in range(len(numList) -1):
        if selectOperation[i][j] == '*':
            result = result * numList[j + 1]
        if selectOperation[i][j] == '+':
            result = result + numList[j + 1]
        if selectOperation[i][j] == '-':
            result = result - numList[j + 1]
        if selectOperation[i][j] == '//':
            if result < 0:
                var = -result // numList[j + 1]
                result = -var
            else:
                result = result // numList[j + 1]
    resultList.append(result)

print(max(resultList))
print(min(resultList))