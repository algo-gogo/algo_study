def solution(a, b, c, d):

    dice = [a, b, c, d]

    dice_count = {x: dice.count(x) for x in set(dice)}
    answer = 0

    if len(dice_count) == 1:
        answer = 1111 * list(dice_count)[0]
    elif len(dice_count) == 2:
        # 3개가 같다면
        if 3 in dice_count.values():
            p = 0
            q = 0
            for key, value in dice_count.items():
                print(key, value)
                if value == 3:
                    p = key
                else:
                    q = key
            answer = (10 * p + q) ** 2
        # 2개가 같다면
        else:
            dice_list = list(dice_count.keys())
            p = dice_list[0]
            q = dice_list[1]
            answer = (p + q) * abs(p - q)
    elif len(dice_count) == 3:
        dice_count = sorted(dice_count.items(), key=lambda x: x[1], reverse=True)
        p = dice_count[0][0]
        q = dice_count[1][0]
        r = dice_count[2][0]
        answer = q * r
    else:
        dice_count = sorted(dice_count.items(), key=lambda x: x[1], reverse=True)
        answer = dice_count[0][0]


    return answer

print(solution(2, 2, 2, 2))