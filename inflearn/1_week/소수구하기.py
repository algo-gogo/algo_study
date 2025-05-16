### https://www.acmicpc.net/problem/1929

input = 20

def find_prime_list_under_number(number):
    result = []
    for n in range(2, number + 1):
        for i in result:
            if i * i <= n and n % i == 0:
                break
        else:
            result.append(n)

    return result

### 6 => 2, 3이기 때문에 for문 돌면서 다 확인할 필요 없고 n보다 작은 소수를 나눠서 확인하면 된다.
# def find_prime_list_under_number(number):
#     result = []
#     for n in range(2, number + 1):
#         for i in result:
#             if n % i == 0:
#                 break
#         else:
#             result.append(n)
#
#     return result

# def find_prime_list_under_number(number):
#     result = []
#     for n in range(2, number + 1):
#         for i in range(2, n):
#             if n % i == 0:
#                 break
#         else:
#             result.append(n)
#
#     return result


result = find_prime_list_under_number(input)
print(result)

###
# 소수는 자기 자신과 1외에는 아무것도 나눌 수 없다.
