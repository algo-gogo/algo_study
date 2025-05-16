
from collections import deque

p1, p2, p3 = map(int, input().split())

p_list = [p1, p2, p3]

print(p_list)

queue = deque()

queue.append((p_list, 0))

def is_end(penguin_list):
    penguin_list.sort()
    if penguin_list[0] + 1 == penguin_list[1] and penguin_list[1] + 1 == penguin_list[2]:
        return True
    return False

result_list = []
while queue:
    p_list, count = queue.popleft()

    if is_end(p_list):
        result_list.append(count)

    min_num = p_list[0]
    mid_num = p_list[1]
    max_num = p_list[2]

    for i in range(mid_num + 1, max_num):
        temp_p_list = [i, mid_num, max_num]
        temp_p_list.sort()
        queue.append((temp_p_list, count + 1))

    for i in range(min_num + 1, mid_num):
        temp_p_list = [min_num, mid_num, i]
        temp_p_list.sort()
        queue.append((temp_p_list, count + 1))

print(min(result_list))
print(max(result_list))
