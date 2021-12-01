# 프로그래머스
# 답지 한번 훑어봄
def create(answer, n):
    if len(answer) == 0:
        return True
    for x, y, a in answer:
        # 기둥
        if a == 0:
            # 땅에 있어야함
            # 다른 기둥이 있어야함
            # 보의 끝부분에 있어야함
            # if y == 0:
            #     continue
            # elif [x, y - 1, 0] in answer:
            #     continue
            # # 보의 끝부분에 있어야함
            # elif [x, y, 1] in answer:
            #     continue
            # else:
            #     return False
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False
        # 보
        else:
            # 한쪽 끝 부분이 기둥 위에 있거나
            # 양쪽 끝부분이 다른 보와 동시에 연결이 되어야한다
            # if [x, y - 1, 0] or [x + 1, y - 1, 0] in answer:
            #     continue
            # elif [x - 1, y, 1] in answer and [x + 1, y, 1] in answer:
            #     continue
            # else:
            #     return False
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        print(x, y, a, b)

        # 기둥이나 보를 설치할 수 있나?
        if b == 0:
            # 삭제가 가능한가?
            answer.remove([x, y, a])
            if create(answer, n) is False:
                answer.append([x, y, a])
        else:
            # 생성이 가능한가?
            if create(answer, n):
                answer.append([x, y, a])
    answer.sort()
    return answer


# print(solution(5, [
#     # 좌표x, 좌표y, 기둥/보(0/1), 삭제/설치(0/1)
#     [1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]
# ]))

print(solution(5, [
    [0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0],
    [1, 1, 1, 0], [2, 2, 0, 1]
]))
