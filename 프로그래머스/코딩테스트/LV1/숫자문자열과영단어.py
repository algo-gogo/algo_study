def solution(s):
    array = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(array)):
        # index = s.find(array2[i])
        # print(index)
        # if index != -1:
        #     iss = s[index:len(array2[i])]
        s = s.replace(array[i], str(i))

    print(s)
    return int(s)

# def solution2(s):
#     array = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#     for i in range(len(array)):
#         index = s.find(array[i])
#         print(index)
#         if index != -1:
#             iss = s[index:len(array[i])]

solution("one4seveneight")