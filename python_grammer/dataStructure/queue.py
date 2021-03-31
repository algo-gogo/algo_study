# 선입 선출

# deque 라이브러리 - 효율적이며, 간단
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(7)
queue.append(1)
queue.append(9)
print(queue[0])
queue.popleft()
print(queue[0])
queue.append(7)
queue.popleft()

print(queue)
queue.reverse()
print(queue)