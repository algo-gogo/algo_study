from collections import deque

def solution(board):
    one_list = []
    two_list = []
    three_list = []
    four_list = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                one_list.append([i, j])
            elif board[i][j] == 2:
                two_list.append([i, j])
            elif board[i][j] == 3:
                three_list.append([i, j])
            elif board[i][j] == 4:
                four_list.append([i, j])
    print(one_list)
    print(two_list)
    print(three_list)
    print(four_list)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    result_list = []
    for x, y in one_list:
        count = 0
        connect_count = 0
        queue.append((x, y, connect_count))
        while queue:
            x, y, connect_count = queue.popleft()
            count += 1
            if connect_count < 3:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                        if board[nx][ny] == 1:
                            queue.append((nx, ny, connect_count + 1))
                            board[nx][ny] = -1
        result_list.append(count)

    for x, y in two_list:
        count = 0
        connect_count = 0
        queue.append((x, y, connect_count))
        while queue:
            x, y, connect_count = queue.popleft()
            count += 1
            if connect_count < 3:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                        if board[nx][ny] == 2:
                            queue.append((nx, ny, connect_count + 1))
                            board[nx][ny] = -1
        result_list.append(count)

    for x, y in three_list:
        count = 0
        connect_count = 0
        queue.append((x, y, connect_count))
        while queue:
            x, y, connect_count = queue.popleft()
            count += 1
            if connect_count < 3:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                        if board[nx][ny] == 3:
                            queue.append((nx, ny, connect_count + 1))
                            board[nx][ny] = -1
        result_list.append(count)

    for x, y in four_list:
        count = 0
        connect_count = 0
        queue.append((x, y, connect_count))
        while queue:
            x, y, connect_count = queue.popleft()
            count += 1
            if connect_count < 3:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                        if board[nx][ny] == 4:
                            queue.append((nx, ny, connect_count + 1))
                            board[nx][ny] = -1
        result_list.append(count)
    print(result_list)
    answer = max(result_list)
    if answer == 1:
        return -1
    else:
        return answer



# print(solution([[3, 2, 3, 2], [2, 1, 1, 2], [1, 1, 2, 1], [4, 1, 1, 1]]))
print(solution([[4, 2, 3, 2], [2, 1, 2, 4], [1, 2, 3, 1], [4, 1, 4, 3]]))
