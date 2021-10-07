# n = int(input())
#
# k = list(map(int, input().split()))
# k.sort()
#
# count = 0
# result = 0
# ### 1 2 2 2 3
# for i in k:
#     count += 1
#     if i == count:
#         result += 1
#         count = 0
#     else:
#         continue
#
# print(result)

n = int(input())

count = 0
result = 0
k = list(map(int, input().split()))
k.sort()

for i in k:
    count += 1
    if i == count:
        result += 1
        count = 0

print(result)
