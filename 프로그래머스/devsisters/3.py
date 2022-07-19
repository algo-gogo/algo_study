
# M: 확실 있음
# S: 확실 없음
# ?: 모름
import copy

def solution(board):
    answer = []

    direction_list = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (1, -1), (-1, -1), (1, 1)]
    num_list = ['1', '2', '3', '4', '5']

    table = []
    for b in board:
        table.append(list(b))
    print(table)

    length = len(table[0])

    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] != '.' and table[i][j] != '?' and table[i][j] != 'M':
                target = 0
                target_list = []
                for d in direction_list:
                    nx = i + d[0]
                    ny = j + d[1]
                    if 0 <= nx < 2 and 0 <= ny < length and (table[nx][ny] == '.' or table[nx][ny] == '?'):
                        target += 1
                        target_list.append((nx, ny))
                        table[nx][ny] = '?'

                if int(table[i][j]) == target:
                    for t in target_list:
                        table[t[0]][t[1]] = 'M'
                        for dd in direction_list:
                            nx = i + dd[0]
                            ny = j + dd[1]
                            if 0 <= nx < 2 and 0 <= ny < length and table[nx][ny] in num_list:
                                table[nx][ny] = str(int(table[nx][ny]) - 1)


    print(table)
    for i in range(2):
        answer.append(''.join(t for t in table[i]))



    return answer


print(solution([".1...2", "111.3."]))
# print(solution([".3....", "1..20."]))
