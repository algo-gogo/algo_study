# 수평2칸 수직 한칸
# 수직 두칸 수평 한칸
# 시작점은 입력받은 좌표  나이트는 L자형으로만  -> 말이 움직일 수 있는 경우의 수
# 8 * 8 행렬 안에서

# a1
# location = input()
#
# count = 0
#
# n = location[1]  # 행                # 1
# n = int(n)
# m = location[0]  # 열
# m = int(ord(m)) - int(ord('a')) + 1  # 1
#
# # n, m  1 1
# # 수평으로 두칸 수직 한칸
# types = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (-1, -2), (1, -2)]
#
# x, y = n, m
# for type in types:
#     nx = x + type[0]
#     ny = y + type[1]
#     if nx < 1 or nx > 8 or ny < 1 or ny > 8:
#         continue
#     count += 1
#
# print(count)
#
# #################################
#
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1
#
# steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (-1, -2), (1, -2)]
#
# result = 0
# for step in steps:
#     next_row = row + step[0]
#     next_column = column + step[1]
#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#         result += 1
#
# print(result)


#-----------------------------------------------------------------------

# 8 X 8
# 2가지 방법으로 움직일 수 있다. ->
# 1. 수평으로 두칸 수직으로 한칸
# 2. 수직으로 두칸 수평으로 한칸

# 총 4가지 방법으로 움직일 수 있음
n = input()

dx = [2, -1, 2, 1]
dy = [1, 2, -1, 2]

x = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

startX = x.index(n[0])
startY = int(n[1])

result = 0
for i in range(4):
    nx = startX + dx[i]
    ny = startY + dy[i]
    if 0 < nx < 8 and 0 < ny < 8:
        result += 1

print(result)










