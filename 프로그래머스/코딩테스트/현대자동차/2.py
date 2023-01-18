# 층을 쌓을 때 13이 들어간 층을 뺴고 싶다.
# 예를들어 14층까지 쌓는다고 했을 때 13층을 뺀 13개 층을 쌓는다.
# 140층을 쌓는다고 했을 때 13, 113, 131, 132 ... 이렇게 13일 들어간 곳을 모두 뺀다.
# 입력은 10^18 이하의 자연수이다.
# 입력 14 -> 출력 13
# 입력 999999 -> 950598

def solution(n):

    minus_value = 0
    for i in range(n):
        if '13' in str(i):
            minus_value += 1

    return n - minus_value


print(solution(999999))