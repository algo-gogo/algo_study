# input = 20
#
# ### 1, 1, 2, 3, 5, 8, 13, 21
#
# def fibo_recursion(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibo_recursion(n - 1) + fibo_recursion(n - 2)
#
#
# print(fibo_recursion(input))  # 6765


input = 50

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}


# def fibo_dynamic_programming(n, fibo_memo):
#     for i in range(3, n + 1):
#         if i not in fibo_memo:
#             fibo_memo[i] = fibo_memo[i - 1] + fibo_memo[i - 2]
#
#     return fibo_memo[n]

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo

print(fibo_dynamic_programming(input, memo))