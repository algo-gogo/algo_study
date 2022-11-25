import copy

def solution(paper, n):

    ### 1, 3, 5
    max_value = max(paper)
    for i in range(n):
        copy_paper = copy.deepcopy(paper)
        result_list = []
        for j in range(1, len(paper)):
            length = len(paper) - j
            if j < length:
                for k in range(j):
                    copy_paper[k]

    return max_value


print(solution([7, 3, 5, -2, 9], 2))
print(solution([10, -10], 1))
print(solution([1, 2, 4, 8, 16], 3))
