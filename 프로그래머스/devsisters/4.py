from itertools import combinations

def solution(L):
    per_list = list(combinations(L, len(L)))
    print(per_list)

    t_f_list = []
    for per in per_list:
        breakPoint = 0
        h_list = []

        for index, value in enumerate(per):
            count = 0
            for h in h_list:
                if value[0] <= h:
                    count += 1
            if value[1] != count:
                t_f_list.append(False)
                breakPoint = -1
                break

            h_list.append(value[0])

        if breakPoint != -1:
            t_f_list.append(True)

    index = t_f_list.index(True)

    return list(per_list[index])



print(solution([[7, 0], [5, 0], [5, 3], [6, 1]]))
