def solution(money, costs):
    coin_num_list = [1, 5, 10, 50, 100, 500]
    cost_list = []
    for i in range(len(costs)):
        value = costs[i]
        cost_list.append((value, coin_num_list[i]))
    print(cost_list)

    resultList = []
    dp = []
    while money > 0:
        for i in range(len(cost_list)):
            create = cost_list[i][0]
            won = cost_list[i][1]
            money_won = money // won
            value = create * money_won
            if value == 0:
                value = 1e9
            dp.append((value, create, won * money_won))
        min_value = min(dp)[2]
        print("dp", min(dp))
        print("min_value", min_value)
        resultList.append(min(dp)[0])
        dp = []
        money = money - min_value
        print(money)

    print(resultList)
    return sum(resultList)


# print(solution(4578, [1, 4, 99, 35, 50, 1000]))
print(solution(1999, [2, 11, 20, 100, 200, 600]))
