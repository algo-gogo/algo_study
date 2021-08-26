n = int(input())

array = []
for i in range(n):
    array.append(list(map(int, input())))


def dfs(x, y):
    if x >= 0 and x < n and y >= 0 and y < n:
        if array[x][y] == 0:
            array[x][y] = 1
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
        else:
            return False


result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            result += 1
print(result)

##2개 모두 기억해놓기!!

####################################################

# 백준 - 단지 번호 붙이기

# 1은 집이 있는곳, 0은 집이 없는곳

# 입력: n (지도의 크기 n * n ) , 좌표
# 출력  단지의 개수와  속한 집의 수

# 지도의 크기 입력받기
n = int(input())

# 집정보 입력받기
world = []
for i in range(n):
    world.append(list(map(int, input())))

# 정답을 출력할 리스트 초기화하기
answer = []


# dfs구현
def dfs(x, y):
    if x >= 0 and x < n and y >= 0 and y < n:
        if world[x][y] == 1:
            world[x][y] = 3
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

            return 1
        else:
            return 0
    return 0


# 덩어리 셀 변수와,이전 3의 개수 저장할 변수 초기화하기
count = 0
prev = 0

# 개수세기
for i in range(n):
    for j in range(n):
        if dfs(i, j) == 1:
            # 현재 꺼 셀 변수 초기화하기
            now = 0
            count += 1
            for k in range(n):
                now += world[k].count(3)

            # 지금 센 개수에서 이전 꺼 빼기
            now -= prev
            answer.append(now)
            # 이전꺼는 현재꺼 더해주기
            prev += now
answer.sort()

print(count)
for i in answer:
    print(i)

#####################################################

# from sys import stdin
# n = int(input())
# # 데이터 저장용 공간 matrix
# matrix = [[0]*n for _ in range(n)]
# # 방문 내역 저장용 visited
# visited = [[0]*n for _ in range(n)]
#
# # matrix에 아파트 유무 0과 1 저장
# for i in range(n):
#     line = stdin.readline().strip()
#     for j, b in enumerate(line):
#         matrix[i][j] = int(b)
#
# # 방향 확인용 좌표 dx와 dy
# # 중앙을 기준으로 좌/우/위/아래
# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1, -1]
#
# # DFS 함수 정의
# def dfs(x, y, c):
#     visited[x][y] = 1   # 방문 여부 표시
#     global nums            # 아파트 단지 수를 세기위한 변수
#     # 아파트가 있으면 숫자를 세어줍니다.
#     if matrix[x][y] == 1:
#         #matrix[x][y] = c # 아파트 단지별 숫자 표시용
#         nums += 1
#     # 해당 위치에서 좌/우/위/아래 방향의 좌표를 확인해서 dfs 적용
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < n:
#             if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
#                 dfs(nx,ny, c)
#
# cnt = 1 # 아파트 단지 세기 위한
# numlist = [] # 아파트 단지별 숫자
# nums=0 # 아파트 수
# for a in range(n):
#     for b in range(n):
#         if matrix[a][b] == 1 and visited[a][b] == 0:
#             dfs(a,b,cnt)
#             numlist.append(nums)
#             nums = 0
# #            cnt += 1 # 아파트 단지 별 표시용
#
# print(len(numlist))
# for n in sorted(numlist):
#     print(n)
