### 이거와 비슷
### https://leetcode.com/problems/sliding-window-maximum

# def solution(stones, k):
#     answer = 0
#
#     while True:
#         zero_count = 0
#         for i in range(len(stones)):
#             if stones[i] == 0:
#                 zero_count += 1
#             else:
#                 zero_count = 0
#             if zero_count == k:
#                 return answer
#             if stones[i] != 0:
#                 stones[i] -= 1
#         answer += 1

# def solution(stones, k):
#
#     min_value = 1e9
#     for i in range(0, len(stones) - k):
#         max_value = max(stones[i:i + k])
#         if max_value < min_value:
#             min_value = max_value
#
#     return min_value

# def solution(distance, rocks, n):
#     answer = 0
#     start, end = 0, distance
#
#     rocks.sort()  # 정렬되어 있지 않은 상태이기 때문에 정렬해야한다.
#
#     # 이분 탐색
#     while start <= end:
#         mid = (start + end) // 2  # 중간값을 구한다.
#         del_stones = 0  # 제거한 돌을 카운트하기 위한 변수
#         pre_stone = 0  # 기준이되는 돌(시작지점)
#         for rock in rocks:  # 징검다리를 돌면서
#             if rock - pre_stone < mid:  # 돌사이의 거리가 가정한 값보다 작으면 제거한다.
#                 del_stones += 1
#             else:  # 아니라면 그 돌을 새로운 기준으로 세운다.
#                 pre_stone = rock
#
#             if del_stones > n:  # 제거된 돌이 문제 조건 보다 크면 for문을 나온다
#                 break
#
#         if del_stones > n:  # 제거된 돌이 너무 많으면 가정한 값이 큰 것이므로 범위를 작은 쪽으로 줄인다.
#             end = mid - 1
#         else:  # 반대라면 큰 쪽으로 줄인다.
#             answer = mid
#             start = mid + 1
#
#     return answer

import heapq
from math import inf

def solution(stones, k):
    n = len(stones)

    # 최대 힙 방식으로 각 구간의 최댓값을 구할 것이다.
    queue = []
    answer = inf

    # 먼저 0부터 k - 2 까지 최대 힙에 인덱스와 함께 넣자.
    for i in range(k - 1):
        heapq.heappush(queue, [-stones[i], i])

    # k - 1부턴 하나씩 최대 힙에 넣자.
    # 최대 힙의 맨 앞의 인덱스가 i - k + 1보다 작다면 구간을 벗어난 원소
    # 구간을 벗어난 원소를 전부 pop
    for i in range(k - 1, n):
        heapq.heappush(queue, [-stones[i], i])
        while queue[0][1] < i - k + 1:
            heapq.heappop(queue)
        answer = min(answer, -queue[0][0]) # 답은 각 구간의 최댓값들의 최솟값

    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
