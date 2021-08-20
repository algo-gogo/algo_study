n = int(input())

listNum = []
for i in range(0, n):
    listNum.append(int(input()))

removeSameNum = list(set(listNum))
print(removeSameNum)
removeSameNum.sort()
print(removeSameNum)
