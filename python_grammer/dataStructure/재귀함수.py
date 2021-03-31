# 자기자신을 호출하는 함수
# 중요한 조건 2가지 - 종료조건 -
# 트리구조를 사용해서 이해함  -- 해보기!!!

def factorial_iterative(n):
    result = 1
    for i in range(1, n):
        result *= i
    return result


def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


print(factorial_iterative(5))
print(factorial_recursive(5))


# 과제 - 재귀함수의
def pp(n):
    print(n)
    if n > 0 :
        pp(n - 1)
        pp(n - 1)    # -> 4. for 문을 사용해서도 해보기
    print('-', n)


def pp2(n):
    print(n)
    if n > 0:
        pp(n - 1)
        pp(n - 2)
    print('-', n)


def pp3(n):
    print(n)
    if n > 0:
        pp(n - 1)
        pp(n - 2)
        pp3(n - 1)
    print('-', n)

# 161p