# https://programmers.co.kr/learn/courses/30/lessons/60062
from itertools import permutations


def solution(n, weak, dist):
    answer = 0

    print(weak)
    per_list = list(permutations(dist))
    print(per_list)

    for per in per_list:
        print(per)
        for p in per:
            for w in weak:
                print(w)

    return answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
# print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
