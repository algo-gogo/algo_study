def solution(k, dungeons):

    dungeons.sort(key=lambda x:x[0] - x[1], reverse=True)
    print(dungeons)

    result = 0
    for d in dungeons:
        if k >= d[0]:
            k -= d[1]
            result += 1

    return result


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
