import copy


def solution(maps):
    copy_maps = copy.deepcopy(maps)
    answer = 0

    # 땅 리스트
    land_list = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if dfs(i, j, copy_maps):
                answer += 1

    return answer


def dfs(x, y, maps):
    if 0 <= x < len(maps) and 0 <= y < len(maps[0]):
        if maps[x][y] != 1:
            maps[x][y].extend(1) # 방문했다고 표시
            print(maps)
            dfs(x - 1, y, maps)
            dfs(x, y - 1, maps)
            dfs(x + 1, y, maps)
            dfs(x, y + 1, maps)
            return True
        else:
            return False

print(solution(
    ['AABCA.QA', 'AABC..QX', 'BBBC.Y..', '.A...T.A', '....EE..', '.M.XXEXQ', 'KL.TBBBQ']))
print(solution(['XY..', 'YX..', '..YX', '.AXY']))

# 각 나라는 알파벳 대문자로 구별
# 빈 영토는 .
# 가장 영토가 넓은 나라가 승리
# 만약 영토가 같다면, 알파벳 순서가 뒤인 나라가 승리
# 승리한 나라는 자신보다 영토가 작은 나라를 점령
# 전쟁이 일어나기 전 초기 상태의 지도 maps
# 전쟁이 끝난 후의 가장 많은 영토를 차지한 나라의 넓이(격자 칸의 개수)를 return


# print(solution(
#     ['AABCA.QA', 'AABC..QX', 'BBBC.Y..', '.A...T.A', '....EE..', '.M.XXEXQ', 'KL.TBBBQ']))
# print(solution(['XY..', 'YX..', '..YX', '.AXY']))
