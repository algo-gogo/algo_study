### https://codlingual.tistory.com/252

from itertools import combinations


def meet_poing(line1, line2):
    a, b, e = line1
    c, d, f = line2
    if a * d == 0 and b * c == 0:
        return None

    x = (b * f - e * d) / (a * d - b * c)
    y = (e * c - a * f) / (a * d - b * c)

    return x, y


def solution(line):
    combi_list = list(combinations(line, 2))
    print(combi_list)

    point_list = []
    x_list = []
    y_list = []
    for i in range(len(combi_list)):
        a, b = combi_list[i]
        point_x_y = meet_poing(a, b)
        if point_x_y is not None:
            x = point_x_y[0]
            y = point_x_y[1]
            x_list.append(x)
            y_list.append(y)
            if x.is_integer() and y.is_integer():
                point_list.append((int(x), int(y)))

    print(point_list)
    x_max = int(max(x_list))
    x_min = int(min(x_list))
    y_max = int(max(y_list))
    y_min = int(min(y_list))

    answer = ['.' * (x_max - x_min + 1)] * (y_max - y_min + 1)
    # 각 좌표마다 * 그리기
    for point in point_list:
        x, y = point
        answer[y_max - y] = answer[y_max - y][:x - x_min] + '*' + answer[y_max - y][x - x_min + 1:]

    return [''.join(ans) for ans in answer]


# print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
# print(solution([[1, -1, 0], [2, -1, 0]]))
# print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))
