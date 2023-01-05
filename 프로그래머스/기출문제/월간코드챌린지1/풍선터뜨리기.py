def solution(a):
    if len(a) == 1:
        return 1
    if len(a) == 2:
        return 2

    left = a[0]
    right = a[-1]

    left_list = []
    right_list = []
    for i in a:
        if i < left:
            left_list.append(i)
            left = i

    for i in a[::-1]:
        if i < right:
            right_list.append(i)
            right = i

    left_list.append(a[0])
    right_list.append(a[-1])
    s = left_list + right_list
    s = list(set(s))

    return len(s)


print(solution([9, -1, -5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
