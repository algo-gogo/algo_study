from collections import Counter


def solution(N, A, B):
    C = A + B

    c_counter = Counter(C).most_common()

    c_counter.sort(key=lambda x: (x[1]), reverse=True)

    print(c_counter)
    result = 0
    j = 0
    for i in range(N, 0, -1):
        try:
            result += i * c_counter[j][1]
            j += 1
        except:
            pass

    return result

print(solution(5, [2, 2, 1, 2], [1, 3, 4, 4]))
