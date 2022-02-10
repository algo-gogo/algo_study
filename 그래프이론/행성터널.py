# https://www.acmicpc.net/problem/2887
# 5
# 11 -15 -15
# 14 -5 -15
# -1 -1 -5
# 10 -4 -1
# 19 -4 19

from itertools import combinations

def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
parent = [0] * (n + 1)

edges = []
result = 0

for i in range(1, n + 1):
    parent[i] = i

dList = []
for i in range(n):
    a, b, c = map(int, input().split())
    dList.append((i + 1, a, b, c))
print(dList)
cList = list(combinations(dList, 2))
print(cList)

for i in cList:
    cost = min(abs(i[0][1] - i[1][1]), abs(i[0][2] - i[1][2]), abs(i[0][3] - i[1][3]))
    edges.append((cost, i[0][0], i[1][0]))

edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)