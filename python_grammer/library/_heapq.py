# 파이썬의 힙 기능 - heapq라이브러리
# 우선순위 큐 기능을 구현하고자 할 때 사용 - 이진 트리 구조다.
# 파이썬의 힙은 최소 힙으로 구성 - 최상단 원소 가장 작은 원소
# 힙에 삽입 -> heapq.headpush()  뺄 때 -> heapq.headpop()

import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# 파이썬에서는 최대힙을 제공하지 않음 - 최대 힙을 구현해야 할 때는 원소의 부호를 임시로 변경하는 방식이 사용



def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result
