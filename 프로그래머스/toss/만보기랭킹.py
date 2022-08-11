def solution(steps_one, names_one, steps_two, names_two, steps_three, names_three):

    toss_user = {}
    for i in range(len(steps_one)):
        try:
            toss_user[names_one[i]] += steps_one[i]
        except:
            toss_user[names_one[i]] = steps_one[i]

    for i in range(len(steps_two)):
        try:
            toss_user[names_two[i]] += steps_two[i]
        except:
            toss_user[names_two[i]] = steps_two[i]

    for i in range(len(steps_three)):
        try:
            toss_user[names_three[i]] += steps_three[i]
        except:
            toss_user[names_three[i]] = steps_three[i]

    toss_user_sort = sorted(toss_user.items(), key=lambda item: (-item[1], item[0]))

    print(toss_user_sort)
    result_list = []
    for i in toss_user:
        result_list.append(i)

    return result_list


print(solution([1, 2, 3], ["james", "bob", "alice"],
               [10, 20, 30], ["james", "alice", "bob"],
               [1000, 1, 1], ["bob", "alice", "james"]))

print(solution([0, 5, 1], ["evan", "ed", "evan"],
               [9999], ["rose"],
               [1], ["richard"]))
