def solution(topping):
    answer = 0
    length = len(set(topping))

    for i in range(1, len(topping) + 1):
        topping_slice = topping[:i]
        topping_slice = set(topping_slice)
        topping_slice2 = topping[i:]
        topping_slice2 = set(topping_slice2)
        if len(topping_slice) == len(topping_slice2):
            answer += 1
        elif len(topping_slice) > len(topping_slice2):
            break

    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
# print(solution([1, 2, 3, 1, 4]))
