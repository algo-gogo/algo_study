import copy


def solution(num_teams, remote_tasks, office_tasks, employees):
    home = []
    team = [[] for i in range(num_teams)]
    office_team = [False for i in range(num_teams)]
    for idx, i in enumerate(employees):
        split = i.split()
        for temp in split:
            if temp in office_tasks:
                office_team[int(split[0]) - 1] = True

        home_flag = False
        for j_idx, j_val in enumerate(split):
            if j_idx == 0:
                team[int(j_val) - 1].append(idx + 1)
                continue
            if j_val in office_tasks:
                home_flag = False
                break
            if j_val in remote_tasks:
                home_flag = True
                continue
        if home_flag:
            home.append(idx + 1)

    team_number_copy = copy.deepcopy(team)

    for i in home:
        for j in team_number_copy:
            for k in j:
                if k == i:
                    j.remove(i)

    for idx, i in enumerate(team_number_copy):
        if len(i) == 0:
            home.remove(team[idx][0])

    return home