# def solution(v, q):
#     answer = []
#     for cmd_list in q:
#         a = cmd_list[0]
#         b = cmd_list[1]
#         c = cmd_list[2]
#         if a == 1:
#             answer.append(sum(v[b: c + 1]))
#         elif a == 2:
#             v[b] = c
#         else:
#             continue
#
#     return answer


def solution(v, q):
    answer = []
    total_sum = {}
    for i in range(0, len(v)):
        total_sum[i] = sum(v[:i + 1])
    print(total_sum)
    print(v)
    print(q)

    for cmd_list in q:
        a = cmd_list[0]
        b = cmd_list[1]
        c = cmd_list[2]
        if a == 1:
            answer.append(total_sum[c] - total_sum[b - 1])
        else:
            diff = c - v[b]
            for i in range(b, len(total_sum)):
                total_sum[i] = total_sum[i] + diff

    print(answer)


print(solution([1, 2, 3, 4, 5], [[1, 2, 4], [2, 3, 8], [1, 2, 4]]))
