def recursiveFunction1(n):
    print(n)
    if n > 0:
        recursiveFunction1(n - 1)
        recursiveFunction1(n - 1)
    print('-', n)

# recursiveFunction1(3)

def recursiveFunction2(n):
    print(n)
    if n > 0:
        recursiveFunction2(n - 1)
        recursiveFunction2(n - 2)
    print('-', n)

# recursiveFunction2(3)

def recursiveFunction3(n):
    print(n)
    if n > 0:
        recursiveFunction3(n - 1)
        recursiveFunction3(n - 2)
        recursiveFunction3(n - 1)
    print('-', n)

recursiveFunction3(3)

# 재귀함수 나올 때 적용해보기
# DFS에 적용해보기

# 그림은 위키에

