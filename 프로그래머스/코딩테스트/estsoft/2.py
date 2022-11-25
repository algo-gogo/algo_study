from collections import Counter
from collections import deque

def queue_count(queue):
    length = len(queue) // 3
    count_dic = dict(Counter(queue))

    for key, value in count_dic.items():
        if value != length:
            return False

    return True

def copy_queue_and_answer(queue_popleft, queue_answer, num):
    copy_queue = queue_popleft[:]
    copy_answer = queue_answer[:]
    copy_answer[num] += 1
    copy_queue.append(num + 1)

    return copy_queue, copy_answer

def solution(queue):
    answer = [0, 0, 0]

    print(queue)

    q = deque()
    q.append((queue, answer))
    print(q)
    while q:
        queue_popleft, queue_answer = q.popleft()
        if queue_count(queue_popleft):
            return queue_answer
        else:
            del queue_popleft[0]

            copy_queue, copy_answer = copy_queue_and_answer(queue_popleft, queue_answer, 0)
            q.append((copy_queue, copy_answer))

            copy_queue, copy_answer = copy_queue_and_answer(queue_popleft, queue_answer, 1)
            q.append((copy_queue, copy_answer))

            copy_queue, copy_answer = copy_queue_and_answer(queue_popleft, queue_answer, 2)
            q.append((copy_queue, copy_answer))


    return answer


print(solution([2, 1, 3, 1, 2, 1]))
# print(solution([3, 3, 3, 3, 3, 3]))
# print(solution([1, 2, 3]))
