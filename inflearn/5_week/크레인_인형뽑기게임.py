def solution(board, moves):
    answer = 0

    print(board)
    print(moves)

    result_list = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                result_list.append(board[i][move-1])
                board[i][move-1] = 0
                break

        temp_result = 0
        for i in range(len(result_list)):
            if temp_result != result_list[i]:
                temp_result = result_list[i]
            else:
                result_list.pop(i)
                result_list.pop(i - 1)
                answer += 2
                break

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))