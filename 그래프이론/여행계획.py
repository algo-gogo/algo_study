# n개의 여행지 1~N
# 여행지 사이에 연결하는 도로가 존재 - 양방향 이동 가능
# 여행 계획을 세운 뒤 여행이 가능한지 여부
# 입력
# 여행지의 수 n 여행계획에 속한 도시 수 m
# n개 줄에 걸쳐 n * n 행렬
# 1이면 연결 0 이면 연결x
# 마지막줄에 여행지 번호

# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3

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

n, m = map(int, input().split())

parent = [0] * (n + 1)

edges = []
result = 0

graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    parent[i] = i

print("parent", parent)

for i in range(n):
    l = list(map(int, input().split()))
    for index, j in enumerate(l):
        if j == 1:
            graph[i + 1].append(index + 1)
            union_parent(parent, i + 1, index + 1)

print("graph", graph)
print("parent", parent)

# 2 3 4 3
# plan = set(map(int, input().split()))
#
# resultList = []
# for i in plan:
#     result = find_parent(parent, i)
#     resultList.append(result)
#
# print(set(resultList))
#
# if len(set(resultList)) > 1:
#     print("NO")
# else:
#     print("YES")


####################
plan = list(map(int, input().split()))

result = True
for i in range(len(plan) - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        result = False

if result:
    print("YES")
else:
    print("NO")
