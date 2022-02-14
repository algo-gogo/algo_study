# g개의 탑승구
# p개의 비행기가 차례대로 도착할 예정
# i 번째 비행기를 1번부터 g(i)번째 탑승구 중 하나에 영구적으로 도킹
# 다른 비행기가 도킹하지 않은 탑승구에만 도킹

# 어떠한 탑승구에도 도킹할 수 없는 비행기가 나오는 경우 공항의 운행을 중지
# 최대한 많은 비행기를 공항에 도킹
# 최대 몇 대 도킹할 수 있는지 출력

# 입력
# 탑승구 g
# 비행기 수 p
# p개의 줄에 각 비행기가 도킹할 수 있는 탑승구 정보 g(i)
# i 번째 비행기가 1번부터 g(i)번째 탑승구 중 하나에 도킹할 수 있다는 의미

# 4
# 3
# 4
# 1
# 1

# 4
# 6
# 2
# 2
# 3
# 3
# 4
# 4

g = int(input())
p = int(input())

air = []
for i in range(p):
    a = int(input())
    air.append(a)

# air.sort()
print(air)

dock = [False for _ in range(g + 1)]
dock[0] = True
print(dock)
isFinish = False

def findDockTrue(a):
    if dock[a]:
        if a == 0:
            return False
        a -= 1
        return findDockTrue(a)
    else:
        dock[a] = True
        return True


for index, a in enumerate(air):
    aa = findDockTrue(a)
    print(aa)
    if not aa:
        break

print(dock)
count = 0
for i in dock:
    if i:
        count += 1

print(count - 1)

#########################

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

g = int(input())
p = int(input())
parent = [0] * (g + 1)

for i in range(1, g + 1):
    parent[i] = i

result = 0
for _ in range(p):
    data = find_parent(parent, int(input()))
    if data == 0:
        break
    union_parent(parent, data, data - 1)
    result += 1

print(result)
