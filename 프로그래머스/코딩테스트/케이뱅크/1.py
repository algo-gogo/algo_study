import math

def solution(card):
    # 인덱스 0: 적립 포인트
    # 1 ~ 12: 1 ~ 12월
    result = [0] * 13
    print(result)

    # 할부가 1이면 1% 적립
    for c in card:
        c = c.split()
        # 날짜
        date = c[0].split('/')
        month = int(date[0])
        # 금액
        price = int(c[1])
        # 할부개월
        installment = int(c[2])

        if installment == 1:
            result[0] += math.ceil(price * 0.01)
            result[month] += price
            continue
        # 다음 해로 넘어가는 청구 금액은 12/31에 청구
        if month + installment - 1 > 12 and month != 12:
            per_month_price = math.ceil(price / installment)
            result[month] += per_month_price
            divide = installment - 1
            for i in range(month + 1, 13):
                if i != 12:
                    result[i] += per_month_price
                    divide -= 1
                else:
                    result[12] += per_month_price * divide
        elif month == 12:
            result[0] += math.ceil(price * 0.01)
            result[month] += price
        else:
            result[month] += math.ceil(price / installment)
            for i in range(1, installment):
                result[month + i] += math.ceil(price / installment)

    return result


print(solution(
    ["02/05 15000 2", "03/11 5541 1", "03/31 10000 3", "03/31 100 1", "05/15 10000 2", "10/10 12345 1", "11/22 5999 4",
     "12/01 901 10"]
))

print(solution(
    ["02/01 12001 12", "12/30 101 2"]
))
