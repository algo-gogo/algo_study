# 매일매일의 환율 변화가 담긴 배열 rates로 환율 투자
# 환율은 원달러 환율을 나타내며 1달러를 사는데 필요한 원화의 가격을 의미합니다.
# 예를 들어, 1200원이면 1달러를 1200원에 사는 것을 의미합니다.
# 아래와 같은 규칙을 지키면서 가상 환율 투자를 해야합니다.
# 1. 초기에는 k원을 가지고 있습니다.
# 2. 환전은 1달러 단위로만 가능합니다.
# 3. 하루에 최대 1달러만 살 수 있고 최대 1달러만 가지고 있을 수 있습니다. 즉 1달러를 산 후에는 가지고 있는 1달러를 팔기 전까지 다시 살 수 없습니다.
# 4. 가지고 있을 수 있는 원화에는 제한이 없습니다.
# 최대 원화는?
# 예시
# k=1000, rates=[1200, 1000, 1100, 1200, 900, 1000, 1500, 900, 750, 1100]
# 1일차: 가지고 있는 원화로 1달러를 살 수 없다.
# 2일차: 1000원으로 1달러를 산다.
# 3일차: 없음
# 4일차: 1달러를 1200원에 판다.
# 5일차: 900원으로 1달러를 산다.
# 6일차: 없음
# 7일차: 1달러를 1500원에 판다.
# 8일차: 없음
# 9일차: 750원으로 1달러를 산다.
# 10일차: 1달러를 1100원에 판다.


def solution(k, rates):
    dp = [0] * len(rates)
    dp[0] = k
    print(dp)
    is_dollar = False

    for i in range(len(rates)):
        print(i)
        if i == len(rates) - 1:
            if is_dollar:
                k += min(rates[i], rates[i - 1])
                break
        if k >= rates[i] and not is_dollar:
            if rates[i] < rates[i + 1]:
                k -= rates[i]
                is_dollar = True
                continue
        if is_dollar:
            if rates[i] > rates[i + 1]:
                k += rates[i]
                is_dollar = False
                continue
        else:
            if rates[i] < rates[i + 1]:
                k -= rates[i]
                is_dollar = True
                continue

    return k



# print(solution(1000, [1200, 1000, 1100, 1200, 900, 1000, 1500, 900, 750, 1100]))
# print(solution(1000, [1200, 1000, 1100, 1200, 900, 1000, 1500, 1700, 750, 100]))
print(solution(1000, [1200, 1000, 1100, 1200, 900, 1000, 1500, 900, 750, 550]))
# print(solution(1500, [1500, 1400, 1300, 1200]))
