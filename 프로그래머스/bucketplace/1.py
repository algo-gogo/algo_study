def turn_direct(now_d, after_d):
    if now_d == 'E' and after_d == 'S':
        return "right"
    if now_d == 'E' and after_d == 'N':
        return "left"
    if now_d == 'N' and after_d == 'E':
        return "right"
    if now_d == 'N' and after_d == 'W':
        return "left"
    if now_d == 'W' and after_d == 'N':
        return "right"
    if now_d == 'W' and after_d == 'S':
        return "left"
    if now_d == 'S' and after_d == 'W':
        return "right"
    if now_d == 'S' and after_d == 'E':
        return "left"


def solution(path):
    answer = []
    time = 0
    a = path[0]
    distance = 0
    length = len(path)

    for i in path:
        after_d = i
        now_d = a
        time += 1
        if i == a:
            distance += 1
        else:
            if time != length:
                pass
            else:
                if distance < 5:
                    direction = turn_direct(now_d, after_d)
                    answer.append("Time")
                else:
                    direction = turn_direct(now_d, after_d)
                    answer.append("Time")
                a = i
                distance = 0

    return answer

# print(solution("EEESEEEEEENNNN"))
# print(solution("SSSSSSWWWNNNNNN"))