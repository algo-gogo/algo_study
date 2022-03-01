### 큰 수의 법칙

# n, m, k = map(int, input().split())
#
# nList = list(map(int, input().split()))
#
# nList.sort(reverse=True)
# print(nList)
#
# result = 0
# while m > 0:
#     for i in range(k):
#         result += nList[0]
#         m -= 1
#         if m == 0:
#             break
#     result += nList[1]
#     m -= 1
#
# print(result)


### 숫자 카드 게임

# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     l = list(map(int, input().split()))
#     graph.append(l)
#
# print(graph)
#
# result = 0
# for i in graph:
#     minNum = min(i)
#     if result < minNum:
#         result = minNum
#
# print(result)

### 1이 될 때까지

n, k = map(int, input().split())

result = 0
while n > 1:
    if n % k == 0:
        n = n // k
        result += 1
    else:
        n = n - 1
        result += 1

print(result)