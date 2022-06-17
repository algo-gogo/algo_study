def now_rank(price, value):
    if price >= 900000:
        if value < 24:
            return 'GOLD'
        else:
            return 'VIP'
    if 600000 <= price < 900000:
        if value >= 60:
            return 'VIP'
        else:
            return 'GOLD'
    if 480000 <= price < 600000:
        if value < 24:
            return 'SILVER'
        else:
            return 'GOLD'
    if 360000 <= price < 480000:
        if value >= 60:
            return 'GOLD'
        else:
            return 'SILVER'
    else:
        return 'SILVER'

def solution(periods, payments, estimates):

    result = [[] for _ in range(len(periods))]
    print(result)

    for index, value in enumerate(periods):
        price = sum(payments[index])
        next_month_price = sum(payments[index]) - payments[index][0] + estimates[index]

        print(price)
        print(next_month_price)

        rank = now_rank(price, value)
        next_rank = now_rank(next_month_price, value + 1)
        result[index].append(rank)
        result[index].append(next_rank)

    print(result)

    result_list = [0, 0]
    for r in result:
        if r[0] != 'VIP' and r[1] == 'VIP':
            result_list[0] += 1
        if r[0] == 'VIP' and r[1] != 'VIP':
            result_list[1] += 1

    return result_list


# print(solution([20, 23, 24], [
#     [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],
#     [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],
#     [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]
# ], [100000, 100000, 100000]))

print(solution([24, 59, 59, 60], [
    [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],
    [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],
    [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],
    [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]
], [350000, 50000, 40000, 50000]))
