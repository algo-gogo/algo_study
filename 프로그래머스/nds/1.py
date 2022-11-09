### 문자열 s에 있는 알파벳 중 'a' 'z'를 하나씩 선택
# 선택한 'a' 'z' 사이의 문자열에 다른 'a' 'z'가 없어야 한다.
import copy

def solution(s):
    count = 0

    a_index_list = []
    z_index_list = []
    for i in range(len(s)):
        if s[i] == 'a':
            a_index_list.append(i)
        elif s[i] == 'z':
            z_index_list.append(i)

    print(a_index_list)
    print(z_index_list)
    for a in a_index_list:
        for z in z_index_list:
            copy_s = copy.deepcopy(s)
            if a < z:
                zz = copy_s[a + 1:z]
                print(zz)
                if 'a' not in zz and 'z' not in zz:
                    count += 1
            else:
                zz = copy_s[z + 1:a]
                print(zz)
                if 'a' not in zz and 'z' not in zz:
                    count += 1
    return count

# print(solution("abcz"))
print(solution("zabzczxa"))
# print(solution("abcd"))