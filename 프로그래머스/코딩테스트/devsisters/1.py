def solution(openA, closeB):
    answer = 0

    time_dic = {}
    for i in openA:
        time_dic[i] = 'open'

    for j in closeB:
        time_dic[j] = 'close'

    print(time_dic)
    time_list = sorted(time_dic.items(), key=lambda item: item[0])
    print(time_list)

    for time in range(len(time_list) - 1):
        if time_list[time][1] == 'open':
            answer += time_list[time + 1][0] - time_list[time][0]
        else:
            pass

    return answer


# print(solution([3, 5, 7], [4, 10, 12]))
print(solution([4, 7, 9, 16], [2, 5, 12, 14, 20]))
