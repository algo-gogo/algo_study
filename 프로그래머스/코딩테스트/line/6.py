def sell(purchase_list, sell_list):
    buy_amount = min(purchase_list[3], sell_list[3])
    amount = sell_list[4] * buy_amount
    # 판매자의 계좌
    purchase_list[4] += amount
    # 구매자의 계좌
    sell_list[4] -= amount
    return purchase_list, sell_list


def find_purchase(price, purchase_list):
    result = []
    for i in purchase_list:
        if i[4] > price:
            result.append(i)
            result.append(i)
    result.sort()
    if len(result) == 0:
        return 0
    print("result", result)
    return result[0]


def solution(req_id, req_info):
    answer = []

    request_result = []

    for i in range(len(req_id)):
        result = []
        value_id = req_id[i]
        value = req_info[i]
        result.append(i)
        result.append(value_id)
        result.append(value[0])
        result.append(value[1])
        result.append(value[2])
        result.append('pending')
        request_result.append(result)

    # index, 이름, type, amount, price, 판매/구매 상태
    print(request_result)

    # sale 판매
    sale_list = []
    for i in request_result:
        if i[2] == 1:
            sale_list.append(i)

    # purchase 구매
    purchase_list = []
    for i in request_result:
        if i[2] == 0:
            purchase_list.append(i)

    print(sale_list)
    print(purchase_list)
    print("------------")

    for i in sale_list:
        if i[5] == 'pending':
            purchase = find_purchase(i[4], purchase_list)
            if purchase == 0:
                continue
            sells = sell(purchase, i)
            purchase_list.append(sells[0])
            i = sells[1]




    print(purchase_list)
    print(sale_list)


    return answer


# TYPE, AMOUNT, PRICE]
# 구매 요청 0
# 판매 요청 1
print(solution(["William", "Andy", "Rohan", "Rohan", "Louis", "Andy"],
               [[1, 7, 20], [0, 10, 10], [1, 10, 40], [1, 4, 25], [0, 5, 11], [0, 20, 30]]))

# print(solution(["Morgan", "Teo", "Covy", "Covy", "Felix"],
#                [[0, 10, 50], [1, 35, 70], [0, 10, 30], [0, 10, 50], [1, 11, 40]]))
