# 25 5
n, k = map(int, input().split())

# n 이 k로 나누어지면 나눈다.
# n 이 나누어지지 않으면 1을 뺀다.
# 1을 만드는 횟수

result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n = n // k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)
