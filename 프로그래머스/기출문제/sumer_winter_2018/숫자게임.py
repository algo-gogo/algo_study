def solution(A, B):
    answer = 0

    A.sort(reverse=True)
    B.sort(reverse=True)

    # 7 5 3 1
    # 8 6 2 2
    for a in A:
        if a >= B[0]:
            continue
        else:
            answer += 1
            B.pop(0)

    return answer

print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
print(solution([2, 2, 2, 2], [1, 1, 1, 1]))