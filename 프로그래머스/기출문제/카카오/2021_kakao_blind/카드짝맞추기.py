
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, -1]

def solution(board, r, c):
    answer = 0

    select_card = 0
    if board[r][c] != 0:
        answer += 1
        select_card = board[r][c]


    return answer


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
# print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))
