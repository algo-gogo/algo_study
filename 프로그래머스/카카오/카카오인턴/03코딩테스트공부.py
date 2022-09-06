def solution(alp, cop, problems):
    answer = 0

    solve_count = 0
    while solve_count < len(problems):
        problem = problems[solve_count]
        alp_request = problem[0]
        cop_request = problem[1]
        alp_reward = problem[2]
        cop_reward = problem[3]
        time = problem[4]




    return answer


print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
# print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))
