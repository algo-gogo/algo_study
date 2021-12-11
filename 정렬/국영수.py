import operator
n = int(input())

array = []

for i in range(n):
    dic = {}
    dic['name'], dic['korean'], dic['english'], dic['math'] = map(str, input().split())
    dic['korean'] = int(dic['korean'])
    dic['english'] = int(dic['english'])
    dic['math'] = int(dic['math'])
    array.append(dic)

print(array)

resultList = sorted(array, key=lambda dic: (-dic['korean'], dic['english'], -dic['math'], dic['name']))
print(resultList)

for dic in resultList:
    print(dic['name'])