from collections import deque


def bfs(strs, t):
    queue = deque()
    queue.append((t, 0))
    while queue:
        word, count = queue.popleft()
        if word == '':
            return count
        for s in strs:
            if word.startswith(s):
                queue.append((word[len(s):], count + 1))
    return -1


def solution(strs, t):
    answer = bfs(strs, t)

    return answer


print(solution(["ba", "na", "n", "a"], "banana"))
# print(solution(["app", "ap", "p", "l", "e", "ple", "pp"], "apple"))
