# 최근에 방문한 순서대로 중복을 제거하여 보여주고자 한다.
# 고객이 할 수 있는 동작 - 직접 방문(숫자), 뒤로가기(B), 앞으로 가기(F)
# 직접 방문 - 해당 페이지를 방문하고, 이전 방문 종목은 뒤로 가기 목록에 추가, 앞으로 가기 목록은 비워짐
# 뒤록 가기 - 뒤로가기 목록에 종목이 없다면 수행되지 않음, 가장 최근에 방문한 페이지로 이동, 이전 방문 종목은 앞으로 가기 목록에 추가
# 앞으로 가기 - 앞으로 가기 목록에 종목이 없다면 수행되지 않음, 앞으로 가기 목록에 가장 최근에 추가된 종목을 방문하고 앞으로 가기 목록 제거, 이전 방문 종목은 뒤로 가기 목록에 추가
# 모든 동작이 끝나고 난 뒤 고객이 보게 될 방문 목록 출력
def solution(maxSize, actions):
    answer = []

    back = []
    forward = []
    back_number = ''
    forward_number = ''
    for i in range(len(actions)):
        if actions[i] == 'B':
            if len(back) == 0:
                continue
            if back_number != '':

                forward.append(back_number)
                back_number = ''
            answer.pop()
        elif actions[i] == 'F':
            answer.append(answer[0])
            answer.pop(0)
        else:
            answer.append(actions[i])
            if back_number != '':
                back.append(back_number)
                back_number = ''
                forward = []

    print(answer)
    return answer[0:maxSize]

print(solution(3, ["1", "2", "3", "4", "5"])) # ["3", "4", "2"]
# print(solution(1, ["B", "F"])) # []
# print(solution(3, ["1", "3", "2", "B", "4", "F"])) # ["4", "3", "2"]
