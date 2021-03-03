
# queue
from collections import deque

queue = deque()

queue.append(5)
queue.append(6)
queue.append(3)
queue.append(9)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
queueList = list(queue)
print(queueList)

# stack
stack = []
stack.append(3)
stack.append(6)
stack.append(9)
stack.pop()

print(stack)