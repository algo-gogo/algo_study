from collections import deque

def solution(n, times):

    present = 1
    result = 0

    queue = deque()
    queue.append((present, result))

    while queue:
        present, result = queue.popleft()
        if present == 1:
            queue.append((2, times[0]))
            continue
        if present >= n:
            return result
        else:
            for index, value in enumerate(times):
                try:
                    row_length = index + 1
                    queue.append((present + row_length, result + value))
                except:
                    pass

print(solution(4, [2, 3]))
print(solution(5, [2, 4, 5]))
print(solution(6, [1, 2, 3]))
