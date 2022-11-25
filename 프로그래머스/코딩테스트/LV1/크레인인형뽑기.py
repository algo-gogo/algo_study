# def solution(board, moves):
#     bucket = []
#     answer = []
#     for move in moves:
#         for i in range(len(board)):
#             if board[i][move - 1] > 0:
#                 bucket.append(board[i][move - 1])
#                 board[i][move - 1] = 0
#                 if bucket[-1:] == bucket[-2:-1]:
#                     answer += bucket[-1:]
#                     bucket = bucket[:-2]
#                 break
#     return len(answer) * 2

def solution(board, moves):
    resultList = [0, 0]
    result = 0
    for i in moves:
        for j in range(len(board)):
            doll = board[j][i - 1]
            if doll != 0:
                resultList.append(doll)
                board[j][i - 1] = 0
                if resultList[-2] == doll:
                    result += 2
                    del resultList[-1]
                    del resultList[-1]
                break

    print(resultList)
    print(result)
    return result


### 4 3 1 1 3 2 4
solution(
    [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 3],
        [0, 2, 5, 0, 1],
        [4, 2, 4, 4, 2],
        [3, 5, 1, 3, 1]
    ],
    [1, 5, 3, 5, 1, 2, 1, 4])
