def solution(A, B):
    # write your code in Python 3.6
    A = str(A)
    B = str(B)
    try:
        return B.index(A)
    except:
        return -1

# print(solution("53", "1953786"))
print(solution(78, 195378678))
print(solution(57, 153786))