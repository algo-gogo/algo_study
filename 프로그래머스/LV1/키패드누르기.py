def solution(numbers, hand):
    right = [10]
    left = [12]
    result = ""
    for i in numbers:
        if i in (1, 4 ,7):
            left.append(i)
            result += "L"
        elif i in (3, 6, 9):
            right.append(i)
            result += "R"
        else:
            if i == 0:
                i = 11
            leftHand = abs(i - left[-1])
            rightHand = abs(i - right[-1])
            if leftHand % 3 + leftHand // 3 < rightHand % 3 + rightHand // 3:
                result += "L"
                left.append(i)
            if leftHand % 3 + leftHand // 3 > rightHand % 3 + rightHand // 3:
                result += "R"
                right.append(i)
            if leftHand % 3 + leftHand // 3 == rightHand % 3 + rightHand // 3:
                if hand == "right":
                    right.append(i)
                    result += "R"
                else:
                    left.append(i)
                    result += "L"

    return result


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
