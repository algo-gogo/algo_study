# https://programmers.co.kr/learn/courses/30/lessons/92344

def recovery_destroy_board(board, skill):
    start_x, start_y = skill[1], skill[2]
    end_x, end_y = skill[3], skill[4]
    for i in range(start_x, end_x + 1):
        for j in range(start_y, end_y + 1):
            if skill[0] == 1:
                board[i][j] -= skill[5]
            if skill[0] == 2:
                board[i][j] += skill[5]

    return board


def solution(board, skill):
    for s in skill:
        board = recovery_destroy_board(board, s)

    print(board)
    count = 0
    for b in board:
        for j in b:
            if j > 0:
                count += 1
    return count


# print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
#                [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
               [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))
