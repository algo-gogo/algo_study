# 수평2칸 수직 한칸
# 수직 두칸 수평 한칸

# a1
location = input()

count = 0

n = location[1]  # 행                # 1
n = int(n)
m = location[0]  # 열
m = int(ord(m)) - int(ord('a')) + 1  # 1

# n, m  1 1
# 수평으로 두칸 수직 한칸
types = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (-1, -2), (1, -2)]

x, y = n, m
for type in types:
    nx = x + type[0]
    ny = y + type[1]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    count += 1

print(count)

#################################

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (-1, -2), (1, -2)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
