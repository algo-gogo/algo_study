# 요약
# 상하좌우로 붙어 있는 경우가 서로 연결되어 있는것
# N X M의 얼음틀의 모양을 입력받아서 주어졌을 때 ->  생성되는 덩어리 개수

# 입력 -> N (행) M (열) N X M의 행렬을 입력받음
# 출력 -> 덩이리 개수

##
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 11111111110011
# 11100011111111
# 11100011111111


# n, m = map(int, input().split())
#
# array = []
# for i in range(n):
#     array.append(list(map(int, input())))


# def dfs(x, y):
#     if x >= 0 and x < n and y >= 0 and y < n:
#         if array[x][y] == 0:
#             array[x][y] = 1
#             dfs(x - 1, y)
#             dfs(x, y - 1)
#             dfs(x + 1, y)
#             dfs(x, y + 1)
#             return True
#         else:
#             return False

# def dfs(x, y):
#     if x <= -1 or x >= n or y <= -1 or y >= m:  # x >=0 and x < n and y >= 0 and y < n
#         return False
#     if array[x][y] == 0:
#         array[x][y] = 1
#         dfs(x - 1, y)  # 왼   # 재귀함수를 쓰는것이 쓰택의 원리와 비슷
#         dfs(x, y - 1)  # 아
#         dfs(x + 1, y)  # 오
#         dfs(x, y + 1)  # 위
#         return True
#     return False
#
#
# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j):
#             result += 1
#
# print(result)
#####################################################





n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input())))

def dfs(x, y):
    if 0 <= x < n and 0 <= y < m:
        if array[x][y] == 0:
            array[x][y] = 1
            # 상하좌우
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            return True
        return False
    else:
        return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)





