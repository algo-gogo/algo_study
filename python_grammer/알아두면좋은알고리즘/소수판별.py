import math


# 모든 수를 검사하기에는 비효율적
# 대칭적인 특징을 이용해서 경우의 수를 줄일 수 있음
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


# 에라토스테네스의 체
# 매우 빠르지만 메모리가 많이 든다. n개의 크기만큼 리스트 할당해야 하기 때문이다.
# n이 1,000,000 이내로 주어지는 경우 좋음
n = 1000
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

    for i in range(2, n + 1):
        if array[i]:
            print(i, end=' ')
