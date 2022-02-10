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

g = int(input())
p = int(input())

air = []
for i in range(p):
    a = int(input())
    air.append(a)

air.sort()
print(air)

dock = [False for _ in range(g + 1)]
dock[0] = True
print(dock)


def findDockTrue(a):
    if dock[a]:
        if a == 0:
            return
        a -= 1
        findDockTrue(a)
    else:
        dock[a] = True
        return


for index, a in enumerate(air):
    findDockTrue(a)

print(dock)
count = 0
for i in dock:
    if i:
        count += 1

print(count - 1)
