# c, c + 1, c + 3, c + 6, c + 10, c + 15, c + 21, c + 28, c + 36, c + 45
# 1, 3, 6    => 2, 3, 4 ... 등차수열
# b - 1, b + 1, b * 2
# 범위 0 <= x <= 200,000
from collections import deque

def calculate_c(value, time):
    # 1  2  3  4   5
    # 1, 3, 6, 10, 15
    return value + (time * (time + 1) // 2)

def solution(c, b):
    # c: 코니의 처음 위치
    # b: 브라운의 처음 위치
    # queue에 b (시간, 위치)
    b_queue = deque()
    b_queue.append((0, calculate_c(c, 0), b))

    while True:
        time, c_value, b_value = b_queue.popleft()
        if c_value == b_value:
            return time
        elif b_value == 200000 or c_value == 200000:
            return time
        else:
            b_queue.append((time + 1, calculate_c(c, time + 1), b_value + 1))
            b_queue.append((time + 1, calculate_c(c, time + 1), b_value - 1))
            b_queue.append((time + 1, calculate_c(c, time + 1), b_value * 2))

print(solution(11, 2))
# c, c + 1, c + 3, c + 6, c + 10, c + 15, c + 21, c + 28, c + 36, c + 45
# 11, 12, 14, 17, 21, 26, 32, 39, 47, 56
# 2, 4, 8, 16, 17

print("정답 = 3 / 현재 풀이 값 = ", solution(10,3))
print("정답 = 8 / 현재 풀이 값 = ", solution(51,50))
print("정답 = 28 / 현재 풀이 값 = ", solution(550,500))
