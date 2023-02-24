def solution(n, arr1, arr2):
    # binaryNum = format(n, 'b')

    binaryNum = format(22, 'b')
    print(binaryNum)

    binary_arr1 = []
    binary_arr2 = []
    for a1 in arr1:
        binaryNum = format(a1, 'b')
        binaryNum = str(binaryNum)
        if len(binaryNum) != n:
            left_length = n - len(binaryNum)
            binaryNum = '0' * left_length + binaryNum
        binary_arr1.append(binaryNum)
    for a2 in arr2:
        binaryNum = format(a2, 'b')
        binaryNum = str(binaryNum)
        if len(binaryNum) != n:
            left_length = n - len(binaryNum)
            binaryNum = '0' * left_length + binaryNum
        binary_arr2.append(binaryNum)

    print(binary_arr1)
    print(binary_arr2)

    result_list = []
    for i in range(len(binary_arr1)):
        result = ''
        for j in range(n):
            a1 = binary_arr1[i][j]
            a2 = binary_arr2[i][j]
            if a1 == '0' and a2 == '0':
                result += ' '
            else:
                result += '#'

        result_list.append(result)

    print(result_list)

    return result_list

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
