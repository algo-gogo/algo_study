# 5! = 5 * 4 * 3 * 2 * 1

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

# def factorial(n):
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#
#     return result

print(factorial(5))