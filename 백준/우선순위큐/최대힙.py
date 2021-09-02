import heapq
import sys

n = int(sys.stdin.readline())

nList = []
for i in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(nList, -num)
    else:
        if len(nList) == 0:
            print(0)
        else:
            result = heapq.heappop(nList)
            print(-result)
