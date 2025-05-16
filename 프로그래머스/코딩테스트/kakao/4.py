# 1 ~ n 까지의 숫자가 적힌 카드, coin 개수의 동전이 있다.
# 처음 카드 뭉치에서 카드 n/3를 가지고, 교환 가능한 동전 coin개를 가진다.
# 게임은 1라운드부터 시작되며, 각 라운드가 시작될때 카드를 두장 뽑는다.
# 카드 뭉치에 남은 카드가 없으면 게임 종료
# 뽑은 카드는 카드 한장당 동전 한개를 소모해서 가지거나 동전을 소모하지 않고 버릴 수 있다.
# 카드에 적힌 수의 합이 n + 1이 되도록 카드 두 장을 내고 다음라운드로 진행한다.
# 만약 카드 두장을 낼 수 없으면 게임 종료

from collections import deque


def solution(coin, cards):
    rounds = 0

    # 처음에 카드 뭉치에서 카드 n/3를 가지고, 교환 가능한 동전 coin개를 가진다.
    n = len(cards)
    first_n = n // 3
    target_sum = n + 1

    card_queue = deque(cards)

    current_card = []
    for i in range(first_n):
        current_card.append(card_queue.popleft())

    pair_found = False
    while True:
        if len(cards) >= 2:
            # 들고 있는 카드 확인
            for i in range(len(current_card) - 1):
                for j in range(i + 1, len(current_card)):
                    if current_card[i] + current_card[j] == target_sum:
                        pair_found = True
                        break
                if pair_found:
                    break

            if pair_found:
                continue

            # 들고 있는 카드로 target_sum을 못만들면 카드 한장 뽑음
            current_card.append(card_queue.popleft())
            pair_found = False

            for i in range(len(current_card) - 1):
                for j in range(i + 1, len(current_card)):
                    if current_card[i] + current_card[j] == target_sum:
                        pair_found = True
                        coin -= 1
                        # 한장 버림
                        current_card.append(card_queue.popleft())
                        break
                if pair_found:
                    break

            if pair_found:
                continue

            current_card.append(card_queue.popleft())
            pair_found = False
            for i in range(len(current_card) - 1):
                for j in range(i + 1, len(current_card)):
                    if current_card[i] + current_card[j] == target_sum:
                        pair_found = True
                        coin -= 2
                        break
                if pair_found:
                    break
        else:
            break
        rounds += 1

    return rounds


print(solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]))
print(solution(
    3, [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]))
