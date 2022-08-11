from collections import Counter


def solution(tasks):
    counter = Counter(tasks)
    print(counter)
    for c in counter:
        if not (counter[c] == 2 or counter[c] == 3):
            return -1
        else:
            return len(counter)


print(solution([1, 1, 2, 3, 3, 2, 2]))
print(solution([4, 1, 1, 1, 1, 2, 3]))
print(solution([1, 1, 2, 2]))
