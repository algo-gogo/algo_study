def solution(n, words):
    answer = []

    person_num = 0
    num = 0
    word_list = []
    flag = False
    for i in range(len(words)):
        person_num += 1
        person_num = person_num % n
        num = i
        if words[i] in word_list or (word_list and word_list[-1][-1] != words[i][0]):
            flag = True
            break
        word_list.append(words[i])

    if not flag:
        return [0, 0]
    if person_num == 0:
        person_num = n
    answer.append(person_num)
    answer.append(num // n + 1)
    return answer


# print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
# print(solution(5,
#                ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang",
#                 "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
