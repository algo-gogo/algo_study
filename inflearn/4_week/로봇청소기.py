from collections import deque

n, m = map(int, input().split())

# r, c, 방향 d를 준다. (0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽)
r, c, d = map(int, input().split())

n_list = []
# n, m만큼 입력을 받음
for i in range(n):
    array = list(map(int, input().split()))
    n_list.append(array)

print(n_list)

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방향 전환
def get_d_index_when_rotate_to_left(d):
    return (d + 3) % 4


# 후진
def get_d_index_when_go_back(d):
    return (d + 2) % 4

def solution(now_x, now_y, direction, map_list):
    # 방문
    result = 1
    map_list[now_x][now_y] = 2
    queue = deque([(now_x, now_y, direction)])

    while queue:
        x, y, dr = queue.popleft()
        temp_d = dr
        for _ in range(4):
            # 왼쪽 방향
            temp_d = get_d_index_when_rotate_to_left(temp_d)
            nx = x + dx[temp_d]
            ny = y + dy[temp_d]
            if 0 <= nx < n and 0 <= ny < m and map_list[nx][ny] == 0:
                map_list[nx][ny] = 2
                queue.append((nx, ny, dr))
                result += 1
                break

            elif i == 3:
                # 뒤로
                nx = x + dx[get_d_index_when_go_back(dr)]
                ny = y + dy[get_d_index_when_go_back(dr)]
                queue.append((nx, ny, dr))
                if map_list[nx][ny] == 1:
                    return result
    return result


print(solution(r, c, d, n_list))