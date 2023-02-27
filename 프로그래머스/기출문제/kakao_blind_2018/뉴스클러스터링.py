def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    str1_list = []
    str2_list = []
    for i in range(len(str1) - 1):
        slice = str1[i:i + 2]
        if slice.isalpha():
            str1_list.append(slice)

    for i in range(len(str2) - 1):
        slice = str2[i:i + 2]
        if slice.isalpha():
            str2_list.append(slice)

    print(str1_list)
    print(str2_list)

    intersection = 0
    union = 0
    for s1 in str1_list:
        if s1 in str2_list:
            intersection += 1
            union += 1
            str2_list.remove(s1)
        else:
            union += 1

    union += len(str2_list)

    print(intersection)
    print(union)
    if union == 0:
        return 65536
    intersection_union = intersection / union

    return int(intersection_union * 65536)

print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))