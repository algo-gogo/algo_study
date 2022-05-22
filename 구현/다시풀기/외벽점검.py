# https://programmers.co.kr/learn/courses/30/lessons/60062
from itertools import permutations


# def solution(n, weak, dist):
#     print(weak)
#     length = len(weak)
#     cand = []
#     weak_point = weak + [w + n for w in weak] # 1 5 6 10 => 1 5 6 10 13 18 19 22
#
#     for i, start in enumerate(weak):
#         print(start)
#         for friends in permutations(dist):
#             print(friends)
#             count = 1
#             position = start
#             # 친구 조합 배치
#             for friend in friends:
#                 position += friend
#                 # 끝 포인트까지 도달 못했을 때
#                 if position < weak_point[i + length - 1]:
#                     count += 1
#                     position = [w for w in weak_point[i + 1: i + length]
#                                 if w > position][0]
#                     temp = []
#                     for w in weak_point[i + 1: i + length]:
#                         if w > position:
#                             temp.append(w)
#                     position = temp[0]
#                 else:
#                     cand.append(count)
#                     break
#     return min(cand) if cand else -1

def solution(n, weak, dist):

    print(dist)
    length = len(weak)
    weak = weak + [w + n for w in weak]  # 1 5 6 10 => 1 5 6 10 13 18 19 22
    print(weak)
    min_count = 1e9

    per_dist = list(permutations(dist))
    for start in range(length):
        print(per_dist)
        for d in per_dist:
            count = 1
            position = start
            for i in range(1, length):
                next_position = start + i
                diff = weak[next_position] - weak[position]
                if diff > d[count - 1]:
                    position = next_position
                    count += 1
                    if count > len(dist):
                        break
            if count <= len(dist):
                min_count = min(min_count, count)

    if min_count == 1e9:
        return -1
    return min_count


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
# print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
