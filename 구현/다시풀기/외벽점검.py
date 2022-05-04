# https://programmers.co.kr/learn/courses/30/lessons/60062
from itertools import permutations


def solution(n, weak, dist):
    print(weak)
    length = len(weak)
    cand = []
    weak_point = weak + [w + n for w in weak]

    for i, start in enumerate(weak):
        print(start)
        for friends in permutations(dist):
            count = 1
            position = start
            # 친구 조합 배치
            for friend in friends:
                position += friend
                # 끝 포인트까지 도달 못했을 때
                if position < weak_point[i + length - 1]:
                    count += 1
                    position = [w for w in weak_point[i + 1: i + length]
                                if w > position][0]
                else:
                    cand.append(count)
                    break
    return min(cand) if cand else -1


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
# print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
