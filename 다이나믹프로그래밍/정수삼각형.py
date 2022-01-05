# https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    answer = 0
    d = []

    for i in range(0, len(triangle)):
        dd = []
        for j in range(len(triangle[i])):
            if i == 0:
                dd.append(triangle[i][j])
                continue

            print(d[i - 1][i - 1 - j] + triangle[i][j])
            dd.append(d[i-1][i - 1 - j] + triangle[i][j])
        d.append(dd)

    print(d)
    return max(d[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
