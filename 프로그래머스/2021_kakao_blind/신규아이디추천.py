# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    answer = ''
    word_list = ['.', '_', '-']
    for i in new_id:
        if i.isalnum() or i in word_list:
            answer += i

    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4단계
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer

    # 5단계
    answer = 'a' if answer == '' else answer

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7단계
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3 - len(answer))
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
