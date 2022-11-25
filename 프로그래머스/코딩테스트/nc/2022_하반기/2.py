

def solution(music):
    piano = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2, 4, 5],
        4: [3, 5],
        5: [3, 4, 6, 7],
        6: [5, 7],
        7: [5, 6, 8],
        8: [7, 9, 10],
        9: [8, 10],
        10: [8, 9, 11, 12],
        11: [10, 12],
        12: [10, 11]
    }

    position = 1
    count = 0
    while music:
        pop = music.pop(0)
        if position == pop:
            count += 1
            position = pop
        elif position < pop:
            if pop in piano[position]:
                count += 1
                position = pop
            else:
                while True:
                    count += 1
                    position = piano[position][-1]
                    if pop in piano[position]:
                        count += 1
                        position = pop
                        break
        elif position > pop:
            if pop in piano[position]:
                count += 1
                position = pop
            else:
                while True:
                    count += 1
                    position = piano[position][0]
                    if pop in piano[position]:
                        count += 1
                        position = pop
                        break
    return count


print(solution([10, 9, 4, 5, 12]))
print(solution([6, 4, 2, 11]))
