# https://programmers.co.kr/learn/courses/30/lessons/60063

from collections import deque

if [4, 4] in [[4, 3], [4, 4]]:
    print("skdjflskdfj")

def solution(board):
    answer = 0

    print(board)
    queue = deque()
    queue.append(([[0, 0], [0, 1]], 0))
    n = len(board)
    while queue:
        robot_list, time = queue.popleft()
        if [n - 1, n - 1] in robot_list:
            return time
        print(robot_list, time)

        # 오른쪽으로
        move_right = []
        for robot in robot_list:
            nx = robot[0]
            ny = robot[1] + 1
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0:
                    move_right.append([nx, ny])
        if len(move_right) == 2:
            queue.append((move_right, time + 1))

        # 아래쪽
        move_under = []
        for robot in robot_list:
            nx = robot[0] + 1
            ny = robot[1]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0:
                    move_under.append([nx, ny])
        if len(move_under) == 2:
            queue.append((move_under, time + 1))

        # 반 시계 방향 회전 90도 회전
        # dx, dy는 평행, 수직 체크 하는 변수명
        dx = abs(robot_list[0][0] - robot_list[1][0])
        # 평행
        if dx == 0:
            move_unclock = []
            move_unclock.append([robot_list[1][0], robot_list[1][1]])
            nx, ny = robot_list[0][0] + 1, robot_list[0][1] + 1
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0 and board[nx][ny + 1] == 0:
                    move_unclock.append([nx, ny])
            if len(move_unclock) == 2:
                queue.append((move_unclock, time + 1))
        # 수직
        else:
            move_unclock_2 = []
            nx, ny = robot_list[0][0] + 1, robot_list[0][1] - 1
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0 and board[nx - 1][ny] == 0:
                    move_unclock_2.append([nx, ny])
            move_unclock_2.append([robot_list[1][0], robot_list[1][1]])
            if len(move_unclock_2) == 2:
                queue.append((move_unclock_2, time + 1))

        # 시계 방향 회전
        # dx, dy는 평행, 수직 체크 하는 변수명
        # 평행
        if dx == 0:
            move_clock = []
            move_clock.append([robot_list[0][0], robot_list[0][1]])
            nx, ny = robot_list[1][0] + 1, robot_list[1][1] - 1
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0 and board[nx][ny + 1] == 0:
                    move_clock.append([nx, ny])
            if len(move_clock) == 2:
                queue.append((move_clock, time + 1))
        # 수직
        else:
            move_clock_2 = []
            move_clock_2.append([robot_list[1][0], robot_list[1][1]])
            nx, ny = robot_list[0][0] + 1, robot_list[0][1] + 1
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0 and board[nx - 1][ny] == 0:
                    move_clock_2.append([nx, ny])
            if len(move_clock_2) == 2:
                queue.append((move_clock_2, time + 1))

    return answer

print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
