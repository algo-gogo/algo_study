### 시간 초과
# import heapq
# import sys
#
#
# def middle_num(list):
#     list.sort()
#     middle1 = list[len(list) // 2]
#     middle2 = list[len(list) // 2 - 1]
#     if len(list) == 1:
#         return list[0]
#     if len(list) % 2 == 0:
#         return min(middle2, middle1)
#     else:
#         return middle1
#
#
# n = int(sys.stdin.readline())
# nList = []
#
# for i in range(n):
#     num = int(sys.stdin.readline())
#     heapq.heappush(nList, num)
#     print(middle_num(nList))

import sys
import heapq


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    max_h, min_h = [], []

    # max_h[0][1]값을 기준으로 큰 값은 min_h, 같거나 작은 값은 max_h에 삽입
    for _ in range(n):
        num = int(sys.stdin.readline())
        if len(max_h) == len(min_h):
            heapq.heappush(max_h, (-num, num))
        else:
            heapq.heappush(min_h, (num, num))
        if len(max_h) >= 1 and len(min_h) >= 1 and max_h[0][1] > min_h[0][1]:
            max_value = heapq.heappop(max_h)[1]
            min_value = heapq.heappop(min_h)[1]
            heapq.heappush(max_h, (-min_value, min_value))
            heapq.heappush(min_h, (max_value, max_value))
        print(max_h[0][1])