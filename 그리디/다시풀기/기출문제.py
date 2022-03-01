### 모험가 길드

# n = int(input())
# nList = list(map(int, input().split()))
#
# nList.sort()
#
# group = 1
# result = 0
# for i in nList:
#     if group == i:
#         result += 1
#         group = 1
#     else:
#         group += 1
#
# print(result)

### 곱하기 혹은 더하기

# s = list(map(int, input()))
#
# print(s)
# result = 0
# for i in range(len(s) - 1):
#     value = s[i]
#     if value == 0 or value == 1:
#         if result == 0:
#             result = value + s[i + 1]
#         else:
#             result = result + s[i + 1]
#     else:
#         if result == 0:
#             result = value * s[i + 1]
#         else:
#             result = result * s[i + 1]
#
# print(result)

### 문자열 뒤집기

s = list(map(int, input()))

count = 0
firstValue = s[0]
for i in s:
    if i == firstValue:
        pass
    else:
        count += 1
        firstValue = i

# print(count)
if count == 1:
    print(1)
else:
    print(count // 2)