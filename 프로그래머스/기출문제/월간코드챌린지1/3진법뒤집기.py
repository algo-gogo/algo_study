def three(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]

def solution(n):
    n = three(n, 3)
    n_list = list(n)
    n_list.reverse()
    n = ''.join(n_list)
    print(n)
    answer = int(n, 3)

    return answer


print(solution(45))
print(solution(125))