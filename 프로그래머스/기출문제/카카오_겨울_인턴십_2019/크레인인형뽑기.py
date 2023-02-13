def solution(board, moves):
    print(board)
    print(moves)

    result_list = []
    result = 0
    for m in moves:
        for i in range(len(board)):
            if board[i][m - 1] != 0:
                result_list.append(board[i][m - 1])
                board[i][m - 1] = 0
                break
        for i in range(len(result_list) - 1):
            if result_list[i] == result_list[i + 1]:
                result += 2
                result_list.pop(i)
                result_list.pop(i)
                break

    print(result_list)

    return result


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
