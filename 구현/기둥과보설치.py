# 프로그래머스

def create(answer, n):
    for x, y, a in answer:
        if a == 0:
            pass
    pass

def remove(answer, n):

    pass

def solution(n, build_frame):

    answer = []
    for x, y, a, b in build_frame:
        print(x, y, a, b)
        # 기둥이나 보를 설치할 수 있나?
        if b == 0:
            # 삭제가 가능한가?
            remove(answer, n)
            answer.remove([x, y, a])

        else:
            # 생성이 가능한가?
            create(answer, n)
            answer.append([x, y, a])
    return answer


print(solution(5, [
    # 좌표x, 좌표y, 기둥/보(0/1), 삭제/설치(0/1)
    [1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]
]))
