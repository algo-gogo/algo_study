# N X M 크기의 직사각형
# 캐릭터는 상하좌우로 움직일 수 있음 - 바다로 되어있는곳은 X
# (A, B) A: 북쪽으로부터 떨어진 칸의 개수 B: 서쪽으로부터 떨어진 칸의 개수
# 1. 반 시계방향으로부터 갈곳을 정함
# 2. 왼쪽 방향에 아직 가보지 않은 칸이 있다면 회전한 다음 한 칸 전진, 가보지 않은 칸이 없다면 왼쪽으로 회전
# 3. 네 방향 모두 이미 가본 칸이거나 바다로 되어있을 경우 바라보는 방향을 유지한 채로 한칸 뒤로 가고 1단계로 돌아감
# 0: 육지 1: 바다
# 캐릭터가 방문한 칸의 수
# 입력: 4 4
#      1 1 0
#      1 1 1 1
#      1 0 0 1
#      1 1 0 1
#      1 1 1 1
n, m = map(int, input().split())
a, b, direction = map(int, input().split())

graph = []
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(int, input().split())))

result = 0
now = graph[a][b]

result = 0
def dfs(x, y):
    if graph[x][y] == 0:
        global result
        result += 1
        graph[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

dfs(a, b)

print(result)


