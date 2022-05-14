def dfs(board, visited, cur_row, cur_col, depth, remove_flag=False):
    if cur_row < 0 or cur_col < 0 or cur_row >= 6 or cur_col >= 6:
        return depth

    cur_color = board[cur_row][cur_col]
    visited[cur_row][cur_col] = 1

    next_rows = [cur_row - 1, cur_row, cur_row + 1, cur_row]
    next_cols = [cur_col, cur_col -1, cur_col, cur_col + 1]

    max_depth = depth
    for next_row, next_col in zip(next_rows, next_cols):
        if 0 <= next_row < 6 and 0 <= next_col < 6:
            next_color = board[next_row][next_col]
            if cur_color != 0 and cur_color == next_color and visited[next_row][next_col] == 0:
                dc = dfs(board, visited, next_row, next_col, depth+1, remove_flag)
                if dc > max_depth:
                    max_depth = dc
                    if max_depth >=3:
                        remove_flag=True

    if max_depth >= 3 or remove_flag is True:
        board[cur_row][cur_col] = 0

    return max_depth


def solution(macaron):
    board = [[] for _ in range(6)]

    for i in range(6):
        for j in range(6):
            board[i].append(0)

    for maca in macaron:
        col_idx, color = maca
        col_idx = col_idx - 1

        for i in range(5, -1, -1):
            if board[i][col_idx] == 0:
                board[i][col_idx] = color
                row_idx = i
                break

        while True:
            visited = [[] for _ in range(6)]
            for i in range(6):
                for j in range(6):
                    visited[i].append(0)

            max_depth = 0
            for i in range(6):
                for j in range(6):
                    if board[i][j] != 0:
                        dc = dfs(board, visited, i, j, 1, False)
                        if dc > max_depth:
                            max_depth = dc

            # max_depth = dfs(board, visited, row_idx, col_idx, 1)
            if max_depth < 3:
                break

            for j in range(6):
                for i in range(6):
                    if board[i][j] == 0:
                        for k in range(i, 0, -1):
                            board[k][j] = board[k-1][j]
                        board[0][j] = 0

    new_board = []
    for i in range(6):
        new_board.append(''.join(str(board[i][j]) for j in range(6)))
    return new_board

print(solution([[1, 1], [2, 1], [1, 2], [3, 3], [6, 4], [3, 1], [3, 3], [3, 3], [3, 4], [2, 1]]))

# print(solution(
#     [[1, 1], [1, 2], [1, 4], [2, 1], [2, 2], [2, 3], [3, 4], [3, 1], [3, 2], [3, 3], [3, 4], [4, 4], [4, 3], [5, 4],
#      [6, 1]]))