# 플레이 리스트에 등록된 순서에 따라 연속 재생
# 마지막 곡을 재생한 다음 첫 번째 곡부터 다시 재생
# listen_time분 동안 음악을 들을 수 있는 서로 다은 최대 곡 수

def solution(play_list, listen_time):

    p_list = []
    for i in range(sum(play_list)):
        p_list.append([i, i + listen_time])

    s = 0
    re_play_list = []
    for i in play_list:
        re_play_list.append(s + i)
        s += i

    print(p_list)
    print(re_play_list)
    result_list = []
    for p in p_list:
        x = p[0]
        y = p[1]
        index1 = 0
        index1Flag = False
        index2 = 0
        index2Flag = False
        for i in range(len(re_play_list)):
            if x <= re_play_list[i] and index1Flag == False:
                index1 = i
                index1Flag = True
            if y <= re_play_list[i] and index2Flag == False:
                index2 = i
                index2Flag = True
        result_list.append((index1, index2))

    print(result_list)
    r_list = []
    for i in result_list:
        r_list.append(abs(i[0] - i[1]))

    return max(r_list)


print(solution([2, 3, 1, 4], 3))
# print(solution([1, 2, 3, 4], 5))
# print(solution([1, 2, 3, 4], 20))
