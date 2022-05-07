
# 5
# 14 31
# 9 2
# 6 12
# 15 61
# 9 4

# 1
# 14 31

# 5
# 685128 537733
# 810686 382235
# 109019 879121
# 835730 18744
# 503293 239908

# 1
# 685128 537733

from collections import deque

n = int(input())

INF = int(1e9)

MAX_NUM = 1000000

graph = [[] for i in range(MAX_NUM + 1)]


for i in range(1, MAX_NUM + 1):
    graph[i].append((2 * i))
    graph[i].append((2 * i) + 1)
    try:
        graph[2 * i].append(i)
        graph[(2 * i) + 1].append(i)
    except:
        pass

# print(graph)

def bfs(start, end, graph):
    queue = deque()
    queue.append((start, 1))
    while queue:
        value, time = queue.popleft()
        try:
            if end in graph[value]:
                return time
            else:
                for i in graph[value]:
                    queue.append((i, time + 1))
        except:
            pass

start_end_list = []
for i in range(n):
    l = list(map(int, input().split()))
    start_end_list.append(l)

result_list = []
for value in start_end_list:
    start = value[0]
    end = value[1]
    result_list.append(bfs(start, end, graph))

print(result_list)