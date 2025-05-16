# A, B가 n개의 주사위를 가지고 승부하려고 한다.
# 각 주사위의 면은 dice[i]개의 면을 가지고 있으며, 각 면에는 1부터 dice[i]까지의 수가 적혀있다.
# A, B n / 2개의 주사위를 가지고 게임을 진행하며, 각 라운드마다 더 높은 수를 가진 사람이 승리한다.
# A가 승리할 확률이 가장 높아지기 위해서 어떤 주사위를 선택해야 하는지 구하라.
from itertools import combinations


def solution(dice):
    answer = []

    # Function to calculate the probability of A winning against a specific die B
    def calculate_probability(die_A, die_B):
        total_outcomes = len(die_A) * len(die_B)
        winning_outcomes = 0

        for face_A in die_A:
            for face_B in die_B:
                if face_A > face_B:
                    winning_outcomes += 1

        return winning_outcomes / total_outcomes

    # Iterate over each die for A
    for die_A in dice:
        max_probability = 0

        # Iterate over each die for B
        for die_B in dice:
            if die_A != die_B:
                # Calculate the probability of A winning against B
                probability = calculate_probability(die_A, die_B)

                # Update max_probability if the current probability is higher
                if probability > max_probability:
                    max_probability = probability

        # Append the die with the highest probability to the answer list
        answer.append(max_probability)

    # answer에서 1, 2 번째 큰 인덱스 반환
    result = {}
    for i in range(len(answer)):
        result[i + 1] = answer[i]
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    print(result)

    r = []
    for i in range(len(result) // 2):
        r.append(result[i][0])
    r.sort()
    return r


print(solution(
    [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]))

print(solution(
    [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]))

print(solution([[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]))
