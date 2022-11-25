# https://programmers.co.kr/learn/courses/30/lessons/92342
from collections import deque
import copy


# 몇점에 화살을 쏠건지?, 화살 리스트
# queue (0, [0, 0, 0...])
# 어피치를 이기려면 어피치보다 1개 더 많이 쏘거나
# 하나도 쏘지 않고 다른 과녁에 쏨

def bfs(n, info):
    queue = deque()
    queue.append((0, [0 for _ in range(11)]))

    result_list = []

    while queue:
        # focus가 0이 10점에 쏘는것
        focus, arrow = queue.popleft()

        # 다 쐈으니까 info 와 arrow를 비교
        if sum(arrow) == n:
            apeach, lion = 0, 0
            for i in range(11):
                if not (arrow[i] == 0 and info[i] == 0):
                    if arrow[i] >= info[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            result_list.append(((apeach - lion), arrow))

        elif sum(arrow) > n:
            continue
        elif focus == 10:  # 화살을 덜 쐈을 경우
            copy_arrow = copy.deepcopy(arrow)
            copy_arrow[focus] = n - sum(copy_arrow)
            queue.append((focus + 1, copy_arrow))
        else:
            copy_arrow = copy.deepcopy(arrow)
            copy_arrow[focus] = info[focus] + 1
            queue.append((focus + 1, copy_arrow))
            copy_arrow2 = copy.deepcopy(arrow)
            copy_arrow2[focus] = 0
            queue.append((focus + 1, copy_arrow2))

    return result_list


def solution(n, info):
    result_list = bfs(n, info)
    result_list.sort(reverse=True)
    print(result_list)
    if result_list[0][0] <= 0:
        return [-1]
    return result_list[0][1]


# print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
# print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(5, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
# print(solution(5, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
