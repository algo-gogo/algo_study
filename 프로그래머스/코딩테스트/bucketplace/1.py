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
    global result
    answer = []
    time = 0
    real_time = 0
    a = path[0]
    distance = 0
    length = len(path)

    for i in path:
        result = ""
        after_d = i
        now_d = a

        time += 1
        if i == a:
            distance += 1
        else:
            if time == length:
                break
            else:
                if distance < 5:
                    direction = turn_direct(now_d, after_d)
                    if real_time != 0:
                        real_time -= 1
                    result += "Time " + str(real_time) + ": Go straight " + str(distance * 100) + "m and turn " + direction
                    answer.append(result)
                else:
                    direction = turn_direct(now_d, after_d)
                    real_time = time - 5
                    if real_time != 0:
                        real_time -= 1
                    result += "Time " + str(real_time) + ": Go straight" + str(distance * 100) + "m and turn " + direction
                    answer.append(result)
                a = i
                distance = 0
                real_time = time

    if result != "":
        answer.append(result)
    return answer

print(solution("EEESEEEEEENNNN"))
# print(solution("SSSSSSWWWNNNNNN"))