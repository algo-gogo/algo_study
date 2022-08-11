from collections import deque

def solution(money, stocks):

    result_list = [0 for _ in range(len(stocks))]
    print(result_list)
    for i in range(len(stocks)):
        value1 = stocks[i][0]
        money1 = stocks[i][1]
        for j in range(i + 1, len(stocks)):
            value2 = stocks[j][0]
            money2 = stocks[j][1]
            if money1 + money2 <= money:
                money1 += money2
                value1 += value2
                result_list[0] = max(result_list[i], value1)
            else:
                break

    return max(result_list)


print(solution(10, [[1, 1], [3, 5], [3, 5], [4, 9]]))
print(solution(30, [[1, 31]]))
