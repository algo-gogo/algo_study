# https://school.programmers.co.kr/learn/courses/30/lessons/42584

from collections import deque

prices = [1, 2, 3, 2, 3]

def get_price_not_fall_periods(prices):
    answer = []
    prices = deque(prices)
    print(prices)
    while prices:
        pop_queue = prices.popleft()
        period = 0
        for next_price in prices:
            if pop_queue > next_price:
                period += 1
                break
            period += 1
        answer.append(period)

    return answer

# def get_price_not_fall_periods(prices):
#     answer = []
#     for i in range(len(prices)):
#         period = 0
#         for j in range(i + 1, len(prices)):
#             if prices[i] <= prices[j]:
#                 period += 1
#             else:
#                 period += 1
#                 break
#
#         answer.append(period)
#
#     return answer


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))