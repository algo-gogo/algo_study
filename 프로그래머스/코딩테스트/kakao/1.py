def solution(friends, gifts):
    answer = 0

    dict = {}
    for i in range(len(friends)):
        dict[friends[i]] = {'send': {}, 'receive': {}}

    for i in range(len(gifts)):
        gift = gifts[i].split(' ')

        if gift[1] in dict[gift[0]]['send']:
            dict[gift[0]]['send'][gift[1]] += 1
        else:
            dict[gift[0]]['send'][gift[1]] = 1

        if gift[0] in dict[gift[1]]['receive']:
            dict[gift[1]]['receive'][gift[0]] += 1
        else:
            dict[gift[1]]['receive'][gift[0]] = 1

    # 두 사람이 선물을 주고 받은 기록이 있다면 더 많은 선물을 준 사람이 다음 달에 선물을 한개 더 받는다.
    # 두 사람이 선물을 주고 받은 기록이 없거나 같다면 선물 지수가 높은 사람이 다음 달에 선물을 한개 더 받는다.
    # 선물 지수가 같다면 선물을 주고 받지 않는다.
    # 선물지수: 선물을 준 횟수 - 선물을 받은 횟수
    gift_score = 0
    for friend in friends:
        send = dict[friend]['send']
        receive = dict[friend]['receive']

        for s in send:
            if s in receive:
                gift_score += send[s] - receive[s]
            else:
                gift_score += send[s]

        for r in receive:
            if r not in send:
                gift_score -= receive[r]

        dict[friend]['gift_score'] = gift_score
        gift_score = 0

    answerList = []
    for friend in friends:
        send = dict[friend]['send']
        receive = dict[friend]['receive']

        answer = 0
        for s in send:
            if s in receive:
                if send[s] > receive[s]:
                    answer += 1
                if send[s] == receive[s]:
                    if dict[s]['gift_score'] > dict[friend]['gift_score']:
                        answer += 1
            if s not in receive:
                answer += 1

        for f in friends:
            if f == friend:
                continue
            else:
                if f not in send and f not in receive:
                    if dict[friend]['gift_score'] > dict[f]['gift_score']:
                        answer += 1
        answerList.append(answer)

    print('dict', dict)
    print('answerList', answerList)
    return max(answerList)


print(solution(
    ['muzi', 'ryan', 'frodo', 'neo'],
    ['muzi frodo', 'muzi frodo', 'ryan muzi', 'ryan muzi', 'ryan muzi', 'frodo muzi', 'frodo ryan', 'neo muzi']))

# print(solution(
#     ['joy', 'brad', 'alessandro', 'conan', 'david'],
#     ['alessandro brad', 'alessandro joy', 'alessandro conan', 'david alessandro', 'alessandro david']
# ))
