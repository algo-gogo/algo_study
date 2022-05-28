def solution(histogram):
    print(histogram)
    result_list = []

    for i in range(len(histogram[0])):
        flag = 1
        for j in range(len(histogram) - 1, -1, -1):
            if histogram[j][i] == 2:
                flag += 1
            if histogram[j][i] == 1:
                flag = 1
            if histogram[j][i] == 0:
                break
        result_list.append(flag)

    print(result_list)
    answer = 1
    for result in result_list:
        answer *= result

    return answer


# 0 - 비어 있는 부분, 1 - 막대 그래프, 2 - 손상된 부분
# print(solution(
#     [[0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1], [0, 1, 0, 1, 0, 0, 1], [1, 1, 2, 2, 1, 0, 1], [2, 2, 2, 2, 1, 2, 2],
#      [2, 2, 1, 1, 1, 2, 2], [2, 2, 1, 1, 1, 2, 2]]))

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [2, 2, 0, 0, 0], [1, 0, 1, 0, 0], [2, 1, 2, 2, 2], [2, 1, 2, 2, 2]]))
