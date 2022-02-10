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

print("parent", parent)

for i in range(1, n + 1):
    parent[i] = i

for i in range(n):
    l = list(map(int, input().split()))
    graph.append(l)

print("graph", graph)

