from copy import deepcopy

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

#### 다른 답지
# 6종류. 동전. 특정 금액만큼 동전을 생산.
# 최소 비용으로 금액만큼 동전을 생산.

# def solution(money, costs):
#     coin_count = [] * (6)
#     coin = []
#
#     coin.append([costs[0], 1])
#     coin.append([costs[1], 5])
#     coin.append([costs[2], 10])
#     coin.append([costs[3], 50])
#     coin.append([costs[4], 100])
#     coin.append([costs[5], 500])
#     # coin.sort(key=lambda x:x[0])
#     # print(coin)
#
#     # cost_list = [] * 6
#     cost_list = [coin[0][0]]
#
#     for i in range(1,len(coin)):
#         cost, won = coin[i]
#         last_cost = (won // coin[i-1][1]) * coin[i-1][0]
#         coin[i][0] = min(cost, last_cost)
#
#     result = 0
#     current = money
#     for i in range(len(coin)-1, -1, -1):
#         cost, won = coin[i]
#         count = current // won
#
#         result += count * cost
#         current -= count * won
#
#     return result

###
def solution(money, costs):
    money_dict = {
        1: costs[0],
        5: costs[1],
        10: costs[2],
        50: costs[3],
        100: costs[4],
        500: costs[5]
    }

    money_per_dict = {
        1: costs[0],
        5: costs[1] / 5,
        10: costs[2] / 10,
        50: costs[3] / 50,
        100: costs[4] / 100,
        500: costs[5] / 500
    }

    money_list = []
    for coin, cost in money_per_dict.items():
        money_list.append((cost, coin))

    money_list.sort()
    answer = 0

    for _, coin in money_list:
        div_res = money // coin
        money -= div_res * coin
        answer += div_res * money_dict[coin]

    print(answer)
