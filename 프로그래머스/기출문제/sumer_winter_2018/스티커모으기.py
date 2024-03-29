def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    dp = [0] * len(sticker)
    dp[0] = sticker[0]
    dp[1] = sticker[0]
    for i in range(2, len(sticker) - 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])

    dp2 = [0] * len(sticker)
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    return max(dp[-2], dp2[-1])

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))
