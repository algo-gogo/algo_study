# https://programmers.co.kr/learn/courses/30/lessons/60063

from collections import deque

# def turn

def solution(board):
    queue = deque()
    # 좌표와 카운트
    queue.append(((1, 1), (1, 2), 0))
    answer = 0
    return answer


solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]])
