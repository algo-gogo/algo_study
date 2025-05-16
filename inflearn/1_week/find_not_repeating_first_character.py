def find_not_repeating_first_character(string):
    for i in range(0, len(string) - 1):
        character = string[i:i + 1]
        if character not in string[0: i] and character not in string[i + 1: len(string) - 1] and string[i + 1: len(string) - 1] != '':
            print(string[i + 1: len(string) - 1])
            return character

    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))