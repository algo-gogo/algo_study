# start 0,0
# 상하좌우로 움직인다.
# 0(상), 1(하), 2(좌), 3(우)
# 상하좌우로 움직이다가 벽에 막히면 순환하는 구조
# (0, 2)라면 위로 2칸 이동한다.
# 그리고 그 위치를 표시해둔다.
# 만약 표시된 위치면 한칸 더 가서 표시한다. (순환)
# 계속 순환하게 되면 fail 리턴

def solution(graph, direction_list):
    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # 0,0에서 시작
    x, y = 0, 0
    # 0,0에서 시작하니까 1로 바꿔줌
    graph[x][y] = 1
    for direction, num in direction_list:
        nx = x + dx[direction] * num
        ny = y + dy[direction] * num
        if not (0 <= nx < len(graph) and 0 <= ny < len(graph[0])):
            nx = nx % len(graph)
            ny = ny % len(graph[0])
        if graph[nx][ny] == 0:
            graph[nx][ny] = 1
            x, y = nx, ny
        else:
            while_num = 0
            while graph[nx][ny] == 1:
                if dx[direction] == 0:
                    ny += 1
                else:
                    nx += 1
                while_num += 1
                if while_num > len(graph):
                    return "fail"



solution([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [(0, 2), (1, 1), (2, 1), (3, 2)])
