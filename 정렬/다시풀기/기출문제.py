####################################### 국영수
# from operator import itemgetter
#
# n = int(input())
#
#
# dic_list = []
#
# for i in range(n):
#     dic = {}
#     name, korean, english, math = map(str, input().split())
#     dic["name"] = name
#     dic["korean"] = int(korean)
#     dic["english"] = int(english)
#     dic["math"] = int(math)
#     dic_list.append(dic)
#
# print(dic_list)
#
# result_list = sorted(dic_list, key=lambda dic: (-dic['korean'], dic['english'], -dic['math'], dic['name']))
#
# for i in result_list:
#     print(i['name'])

####################################### 안테나
# https://www.acmicpc.net/problem/18310

n = int(input())
n_list = list(map(int, input().split()))

n_list.sort()
print(n_list)

index = len(n_list) // 2 - 1
index2 = len(n_list) // 2

result = 0
for i in n_list:
    result += abs(n_list[index] - i)

result2 = 0
for i in n_list:
    result2 += abs(n_list[index2] - i)

if result <= result2:
    print(n_list[index])
else:
    print(n_list[index2])