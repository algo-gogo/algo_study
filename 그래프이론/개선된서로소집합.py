# https://www.youtube.com/watch?v=Ha0w2dJa2Nk&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=33

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


# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합:', end="")
for i in range(1, v + 1):
    print(find_parent(parent, i), end="")

print()

# 부모 테이블 내용 출력
print('부모 테이블', end="")
for i in range(1, v + 1):
    print(parent[i], end=" ")

# 6 4
# 1 4
# 2 3
# 2 4
# 5 6
