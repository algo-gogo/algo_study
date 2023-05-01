# n_list가 있다.
# n_list에서 숫자를 선택하는데 연속 두개이하로 선택할 수 있다.
# 선택한 다음 숫자는 더할 수 없다.
# n_list에 1, 3, 4, 100, 13, 24, 1이 있다고 하자.
# 1,3 선택하고 100 선택하고 24, 1을 선택하는게 제일 크다.
# n_list의 원소들을 더했을 때 최대값을 구하라.

def solution(n_list):
    dp = [0] * len(n_list)
    dp[0] = n_list[0]
    dp[1] = n_list[0] + n_list[1]

    for i in range(2, len(n_list)):
        if i - 3 >= 0:
            dp[i] = max(dp[i - 2] + n_list[i], n_list[i - 1] + n_list[i] + dp[i-3])
        else:
            dp[i] = max(dp[i - 2] + n_list[i], n_list[i - 1] + n_list[i])

    print(dp)

print(solution([1, 3, 4, 100, 13, 24, 1]))
print(solution([1, 1, 1, 100, 100, 1, 1, 100]))