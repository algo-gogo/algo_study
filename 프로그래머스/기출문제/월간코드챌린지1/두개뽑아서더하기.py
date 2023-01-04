from itertools import combinations

def solution(numbers):
    answer = []

    c = list(combinations(numbers, 2))
    print(c)
    for i in c:
        answer.append(sum(i))

    answer = list(set(answer))
    answer.sort()

    return answer

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))