def solution(numbers, hand):
    right = []
    left = []
    result = ""
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            left.append(i)
            result += "L"
        if i == 3 or i == 6 or i == 9:
            right.append(i)
            result += "R"
        if i == 2 or i == 5 or i == 8 or i == 0:
            lefthand = abs(i - left[-1])
            righthand = abs(i - right[-1])
            if sum(divmod(lefthand, 3)) < sum(divmod(righthand, 3)):
                result += "L"
                left.append(i)
            if sum(divmod(lefthand, 3)) > sum(divmod(righthand, 3)):
                result += "R"
                right.append(i)
            if sum(divmod(lefthand, 3)) == sum(divmod(righthand, 3)):
                if hand == "right":
                    result += "R"
                else:
                    result += "L"
    return result


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
