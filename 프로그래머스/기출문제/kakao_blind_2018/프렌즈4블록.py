def block_bump(board, answer):
    result_list = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + 1 < len(board) and j + 1 < len(board[i]):
                print(i, j, board[i][j], board[i + 1][j], board[i][j + 1], board[i + 1][j + 1])
                if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    result_list.append((i, j))

    print(result_list)
    for x, y in result_list:
        if board[x][y] != '0':
            board[x][y] = '0'
            answer += 1
        if board[x + 1][y] != '0':
            board[x + 1][y] = '0'
            answer += 1
        if board[x][y + 1] != '0':
            board[x][y + 1] = '0'
            answer += 1
        if board[x + 1][y + 1] != '0':
            board[x + 1][y + 1] = '0'
            answer += 1

    return answer


def move_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '0':
                for k in range(i, 0, -1):
                    board[k][j] = board[k - 1][j]
                    board[k - 1][j] = '0'

    return board


def solution(m, n, board):
    answer = 0

    board = list(map(list, board))
    board = move_board(board)
    print(board)
    for i in range(len(board)):
        print(board[i])
    bump_number = block_bump(board, answer)

    if bump_number == 0:
        return answer
    else:
        answer += bump_number
        answer += solution(m, n, board)

    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
