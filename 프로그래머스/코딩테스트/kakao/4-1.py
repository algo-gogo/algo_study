from collections import deque

def solution(coin, cards):
    card_queue = deque(cards)

    rounds = 0
    target_sum = len(cards) + 1

    current_card = []
    for i in range(len(cards) // 3):
        current_card.append(card_queue.popleft())

    while card_queue:
        if len(card_queue) >= 2:
            pair_found = False

            for i in range(len(current_card) - 1):
                for j in range(i + 1, len(current_card)):
                    if current_card[i] + current_card[j] == target_sum:
                        pair_found = True
                        break
            if pair_found:
                card_queue.popleft()
                card_queue.popleft()
            else:
                card_queue.popleft()
                for i in range(len(current_card) - 1):
                    for j in range(i + 1, len(current_card)):
                        if current_card[i] + current_card[j] == target_sum:
                            coin -= 1
                            pair_found = True
                            break

                if pair_found:
                    card_queue.popleft()
                else:
                    card_queue.popleft()
                    for i in range(len(current_card) - 1):
                        for j in range(i + 1, len(current_card)):
                            if current_card[i] + current_card[j] == target_sum:
                                coin -= 2
                                pair_found = True
                                break
                    if pair_found:
                        break
        else:
            break

        rounds += 1

    return rounds

result = solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4])
print(result)