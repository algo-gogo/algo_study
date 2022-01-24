# 학생들에게 0 부터 N번까지의 번호를 부여
# 총 n + 1 팀이 존재
# 선생님은 팀합치기, 같은 팀 여부 확인 연산을 사용 가능
# M개의 연산을 수행할 수 있을 때 같은 팀 여부 확인 연산에 대한 연산 결과 출력

# n, m
# 각 연산
# 팀 합치기 - 0 a b
# 같은 팀 여부 확인 - 1 a b
# a, b 는 N이하의 양의 정수
# 출력: YES or NO

# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1

# NO
# NO
# YES

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

for i in range(1, n + 1):
    parent[i] = i

for i in range(m):
    type, a, b = map(int, input().split())
    if type == 0:
        union_parent(parent, a, b)

    if type == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
