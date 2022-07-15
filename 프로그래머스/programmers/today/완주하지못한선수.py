# https://school.programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    answer = ''
    for i in completion:
        if i in participant:
            participant.remove(i)
    print(participant)
    return participant[0]