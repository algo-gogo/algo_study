# https://school.programmers.co.kr/learn/courses/30/lessons/81303

# def find_true(table):
#     for i in range(len(table)):
#         if table[i][1]:
#             return i
#
# def find_table(table, n):
#     result = ['X' for _ in range(n)]
#     for i in table:
#         result[i[0]] = 'O'
#
#     answer = ''
#     for i in result:
#         answer += i
#     return answer
#
# def solution(n, k, cmd):
#     answer = ''
#
#     print(cmd)
#     table = [[i, False] for i in range(n)]
#     table[k][1] = True
#     print(table)
#
#     delete_list = []
#
#     cmd_one_list = ['C', 'Z']
#     for c in cmd:
#         if c in cmd_one_list:
#             if c == 'Z':
#                 if len(delete_list) == 0:
#                     pass
#                 else:
#                     try:
#                         index = delete_list[-1]
#                         table.insert(index, [index, False])
#                         del delete_list[-1]
#                     except:
#                         pass
#             if c == 'C':
#                 index = find_true(table)
#                 delete_list.append(table[index][0])
#                 del table[index]
#                 try:
#                     table[index][1] = True
#                 except:
#                     table[-1][1] = True
#         else:
#             split = c.split(' ')
#             if split[0] == 'D':
#                 try:
#                     index = find_true(table)
#                     table[index][1] = False
#                     table[index + int(split[1])][1] = True
#                 except:
#                     table[-1][1] = True
#             else:
#                 try:
#                     index = find_true(table)
#                     table[index][1] = False
#                     table[index - int(split[1])][1] = True
#                 except:
#                     table[0][1] = True
#
#     print(table)
#     answer = find_table(table, n)
#
#     return answer

def solution(n, k, cmd):
    answer = ''
    cur = k
    table = {i: [i - 1, i + 1] for i in range(n)}
    table[0] = [None, 1]
    table[n - 1] = [n - 2, None]
    answer = ['O' for _ in range(n)]
    stack = []
    print(table)
    for c in cmd:
        # 삭제
        if c == 'C':
            answer[cur] = 'X'
            prev, next = table[cur]
            stack.append([prev, cur, next])
            if next == None:
                cur = table[cur][0]
            else:
                cur = table[cur][1]
            if prev == None:
                table[next][0] = None
            elif next == None:
                table[prev][1] = None
            else:
                table[prev][1] = next
                table[next][0] = prev
        # 복구
        elif c == 'Z':
            prev, now, next = stack.pop()
            answer[now] = 'O'
            if prev == None:
                table[next][0] = now
            elif next == None:
                table[prev][1] = now
            else:
                table[next][0] = now
                table[prev][1] = now
        else:
            c1, c2 = c.split(' ')
            c2 = int(c2)
            if c1 == 'D':
                for _ in range(c2):
                    cur = table[cur][1]
            else:
                for _ in range(c2):
                    cur = table[cur][0]

    return ''.join(answer)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
# print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
