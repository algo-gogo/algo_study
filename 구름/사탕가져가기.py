from collections import deque

t = input()

v = list(map(int, input().split()))

print(t, v)

result_list = []


def change_person(p):
    if p == 'G':
        return 'F'
    return 'G'


for candy in v:
    print(candy)
    queue = deque()
    # G - 구르미  F - 친구
    queue.append((candy, 'G'))
    while queue:
        candy_num, turn_person = queue.popleft()
        if candy_num <= 0:
            winner = change_person(turn_person)
            result_list.append(winner)
            break
        else:
            next_person = change_person(turn_person)
            queue.append((candy_num - 1, next_person))
            queue.append((candy_num - 3, next_person))

print(result_list)