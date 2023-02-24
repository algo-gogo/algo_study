def solution(n, k, cmd):

    answer = ''

    stack = []
    table = [i for i in range(n)]
    copy_table = table[::]
    print(copy_table)
    print(table)
    present = k

    for c in cmd:
        copy_table.sort()
        split = c.split(' ')
        direction = split[0]
        if direction == 'U':
            d_number = split[1]
            present -= int(d_number)
        elif direction == 'D':
            d_number = split[1]
            present += int(d_number)
        elif direction == 'C':
            value = copy_table[present]
            copy_table.remove(value)
            stack.append(value)
        elif direction == 'Z':
            copy_table.insert(present, stack.pop())
            present += 1

    print(copy_table)
    for i in range(n):
        if table[i] in copy_table:
            answer += 'O'
        else:
            answer += 'X'

    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
