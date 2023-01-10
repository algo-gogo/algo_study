def solution(a):
    if len(a) == 1:
        return 0
    if len(a) == 2:
        return 2

    num_dict = {}
    prev_num = -1
    for i in range(len(a)):
        if i % 2 == 0:
            prev_num = a[i]
        if i % 2 != 0:
            if prev_num == a[i]:
                prev_num = -1
                continue
        if a[i] in num_dict:
            num_dict[a[i]] += 1
        else:
            num_dict[a[i]] = 1

    num_dict = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
    print(num_dict)

    return num_dict[0][1] * 2


print(solution([0]))
print(solution([5, 2, 3, 3, 5, 3]))
print(solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]))
print(solution([0, 0, 3, 1, 2, 1, 3, 4, 0, 1, 4]))
print(solution([0, 3, 1, 6, 0, 2, 0, 7, 1, 3, 4, 0, 5, 1, 1]))
print(solution([5, 0, 2, 0, 9, 2, 6, 2, 2, 7]))