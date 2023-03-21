def toN(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        if mod >= 10:
            rev_base += chr(mod + 55)
        else:
            rev_base += str(mod)

    return rev_base[::-1]

def solution(n, t, m, p):
    answer = ''

    n_list = []
    i = 0
    while len(answer) < t:
        string_n = toN(i, n)
        if string_n == '':
            string_n = '0'
        n_list = n_list + list(string_n)
        i += 1
        if len(n_list) > t * m:
            break

    print(n_list)

    for i in range(t):
        # a = i * m + p - 1
        answer += n_list[i * m + p - 1]

    return answer

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))