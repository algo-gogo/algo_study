def solution(new_id):
    # 1
    new_id1 = new_id.lower()
    print("step1 = ", new_id1)

    # 2
    answer = ''
    wordList = ['.', '_', '-']
    for i in new_id1:
        if i.isalnum() or i in wordList:
            answer += i
    print("step2 = ", answer)

    # 3
    while '..' in answer:
        answer.replace('..', '.')
    print("step3 = ", answer)

    # 4
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    print("step4 = ", answer)

    # 5
    if len(answer) == 0:
        answer = 'a'
    print("step5 = ", answer)

    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    print("step6 = ", answer)

    # 7
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3 - len(answer))

    return answer

print(solution("=.="))