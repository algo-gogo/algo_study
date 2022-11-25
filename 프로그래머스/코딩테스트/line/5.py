def check(num, abilities):
    if len(abilities) == num * 2 + 1:
        return False
    if abilities[num * 2] == abilities[num * 2 + 1]:
        return True
    return False


def solution(abilities, k):
    answer = 0

    abilities.sort(reverse=True)
    print(abilities)

    if len(abilities) % 2 == 0:
        for i in range(len(abilities) // 2):
            if check(i, abilities):
                answer += abilities[i * 2 + 1]
                print("answer", answer)
            else:
                if k > 0:
                    k -= 1
                    print("answer", answer)
                    print(abilities[i * 2])
                    answer += abilities[i * 2]
                else:
                    answer += abilities[i * 2 + 1]
    else:
        for i in range(len(abilities) // 2 + 1):
            if check(i, abilities):
                answer += abilities[i * 2 + 1]
            else:
                if k > 1:
                    k -= 1
                    answer += abilities[i * 2]
                else:
                    if len(abilities) == i * 2 + 1:
                        answer += abilities[i * 2]
                    else:
                        answer += abilities[i * 2 + 1]

    return answer


print(solution([2, 8, 3, 6, 1, 9, 1, 9], 2))
# print(solution([7, 6, 8, 9, 10], 1))
