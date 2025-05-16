def find_max_plus_or_multiply(array):
    result = 0
    print('---')
    for value in array:
        if value <= 1 or result <= 1:
            result += value
        else:
            result *= value

    return result


print("정답 = 728 현재 풀이 값 =", find_max_plus_or_multiply([0, 3, 5, 6, 1, 2, 4]))
print("정답 = 8820 현재 풀이 값 =", find_max_plus_or_multiply([3, 2, 1, 5, 9, 7, 4]))
print("정답 = 270 현재 풀이 값 =", find_max_plus_or_multiply([1, 1, 1, 3, 3, 2, 5]))
