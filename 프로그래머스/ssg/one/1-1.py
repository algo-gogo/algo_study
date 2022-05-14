def two_dice(dice, possible_set):
    for i_index, first_dice in enumerate(dice):
        for j_index, second_dice in enumerate(dice):
            if i_index == j_index:
                continue

            for first_dic in first_dice:
                for second_dic in second_dice:
                    possible_set.add(int(str(first_dic) + str(second_dic)))

    return possible_set


def three_dice(dice, possible_set):
    for i_index, first_dice in enumerate(dice):
        for j_index, second_dice in enumerate(dice):
            for k_index, third_dice in enumerate(dice):
                if i_index == j_index or i_index == k_index or j_index == k_index:
                    continue

                for first_dic in first_dice:
                    for second_dic in second_dice:
                        for third_dic in third_dice:
                            if int(str(first_dic)) != 0:
                                possible_set.add(int(str(first_dic) + str(second_dic) + str(third_dic)))

    return possible_set


def fourth_dice(dice, possible_set):
    for i_index, first_dice in enumerate(dice):
        for j_index, second_dice in enumerate(dice):
            for k_index, third_dice in enumerate(dice):
                for n_index, fourth_dice in enumerate(dice):
                    if i_index == j_index or i_index == k_index or i_index == n_index or j_index == k_index or j_index == n_index or k_index == n_index:
                        continue

                    for first_dic in first_dice:
                        for second_dic in second_dice:
                            for third_dic in third_dice:
                                for fourth_dic in fourth_dice:
                                    if int(str(first_dic)) != 0:
                                        possible_set.add(int(str(first_dic) + str(second_dic) + str(third_dic) + str(fourth_dic)))

    return possible_set


def solution(dice):
    answer = 0
    dice_len = len(dice)
    max_answer = 10 ** dice_len

    dice_all = sum(dice, [])
    print(dice_all)
    possible_set = set(dice_all)

    if dice_len == 2:
        possible_set = two_dice(dice, possible_set)
    elif dice_len == 3:
        possible_set = two_dice(dice, possible_set)
        print(possible_set)
        possible_set = three_dice(dice, possible_set)
        print(possible_set)
    elif dice_len == 4:
        possible_set = two_dice(dice, possible_set)
        possible_set = three_dice(dice, possible_set)
        possible_set = fourth_dice(dice, possible_set)

    for i in range(1, max_answer):
        if i in possible_set:
            continue
        return i


# print(solution([[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]]))
print(solution([[0, 1, 5, 3, 9, 2], [2, 1, 0, 4, 8, 7], [6, 3, 4, 7, 6, 5]]))
