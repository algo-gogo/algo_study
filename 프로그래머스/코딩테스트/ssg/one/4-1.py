from collections import Counter


def find_max(value, two_list):
    answer = two_list[0]
    for i in two_list:
        if value >= i:
            answer = i
        else:
            return answer
    return answer


def solution(weights):
    i = 1
    answer = 1
    two_list = []
    while i < 100000:
        two_list.append(i)
        i = i * 2

    print(two_list)

    counter = dict(Counter(weights))
    print(counter)

    for index, i in counter.items():
        temp = find_max(i, two_list)
        answer = max(answer, temp)

    return answer

print(solution([2, 2, 2, 2, 3, 3, 5, 6]))
# print(solution([3, 3, 3, 3, 3, 3, 12]))
# print(solution([16, 16, 16, 16, 16, 16, 16, 16, 1, 1, 2, 4, 4]))
# print([1])