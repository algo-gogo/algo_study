# 이코테
# N개의 동전을 이용하여 만들 수 없는 최솟값 구하기
# 3, 2, 1, 1, 9 로 만들 수 없는 최소값 -> 8
# 1 1 2 3 9

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

print(target)

# 1 1 2 3 9
# 2 2 2 3 9
# target 1
### 1

# from itertools import combinations
#
# n = int(input())
# data = list(map(int, input().split()))
#
# sum_lst, combi = [], []
# for i in range(1, len(data) + 1):
#     temp = list(combinations(data,i))
#     combi += temp
# print(combi)
# for i in combi:
#     sum_lst.append(sum(i))
# print(sum_lst)
#
# for i in range(1, sum(data)):
#     if i not in sum_lst:
#         print(i)
#         break