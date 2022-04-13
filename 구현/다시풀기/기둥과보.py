# https://programmers.co.kr/learn/courses/30/lessons/60061

def validate(x, y, a, l_list, m_list, n):
    # 기둥
    if a == 0:
        # 바닥
        # 바닥에 있으면서 리스트에 기둥이 없을 경우
        if y == 0 and [x, y] not in l_list:
            return True
        # 보 왼쪽에 기둥이 있을 경우
        if [x, y] in m_list:
            return True
        # 보 오른쪽 위에 기둥이 있을 경우
        if [x - 1, y] in m_list:
            return True
        # 기둥 위에 있을 경우
        if [x, y - 1] in l_list:
            return True
        return False
    # 보
    else:
        # 기둥 위에 있을 경우 - 오른쪽으로
        if [x, y - 1] in l_list:
            return True
        # 기둥 위에 있을 경우 - 왼쪽으로
        if [x + 1, y - 1] in l_list:
            return True
        # 보 옆에 붙을 경우
        if [x + 1, y] in m_list:
            return True
        if [x - 1, y] in m_list:
            return True
        return False


def validate_remove(x, y, a, l_list, m_list, n):
    # 기둥
    if a == 0:
        l_list.remove([x, y])
        # 바닥
        # 바닥에 있으면서 리스트에 기둥이 없을 경우
        if y == 0 and [x, y] not in l_list:
            return True
        # 보 왼쪽에 기둥이 있을 경우
        if [x, y] in m_list:
            return True
        # 보 오른쪽 위에 기둥이 있을 경우
        if [x - 1, y] in m_list:
            return True
        # 기둥 위에 있을 경우
        if [x, y - 1] in l_list:
            return True
        l_list.append([x, y])
        return False
    # 보
    else:
        m_list.remove([x, y])
        # 기둥 위에 있을 경우 - 오른쪽으로
        if [x, y - 1] in l_list:
            return True
        # 기둥 위에 있을 경우 - 왼쪽으로
        if [x + 1, y - 1] in l_list:
            return True
        # 보 옆에 붙을 경우
        ########## 조건 어떻게든 추가해보기 보가 떠있는지 체크
        if [x + 1, y] in m_list and [x, y] in m_list:
            return True
        if [x - 1, y] in m_list and [x, y] in m_list:
            return True

        m_list.append([x, y])
        return False


def solution(n, build_frame):
    answer = [[]]

    # 가로 좌표, 세로 좌표, 0: 기둥   1: 보, 0: 삭제   1: 설치
    print(build_frame)

    # 기둥
    l_list = []
    # 보
    m_list = []

    for index, value in enumerate(build_frame):
        print(value)
        x = value[0]
        y = value[1]
        a = value[2]
        b = value[3]
        if b == 0:
            # 삭제
            validate_remove(x, y, a, l_list, m_list, n)
        else:
            # 설치
            if validate(x, y, a, l_list, m_list, n):
                if a == 0:
                    l_list.append([x, y])
                else:
                    m_list.append([x, y])

    print(l_list)
    print(m_list)

    return answer


# print(solution(5,
#                [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
#                 [3, 2, 1, 1]]))

print(solution(5,
               [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
