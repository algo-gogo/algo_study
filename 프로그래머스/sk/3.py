import math

def solution(width, height, diagonals):
    total_num_with_diags = 0
    for diag in diagonals:
        diag_x, diag_y = diag

        start_diag_pt = (diag_x - 1, diag_y)
        end_diag_pt = (diag_x , diag_y - 1)

        num_to_start_diag = comp_num_path_in_rect((0,0), start_diag_pt)
        num_from_end_diag = comp_num_path_in_rect(end_diag_pt, (width, height))
        num_with_diag = (num_to_start_diag * num_from_end_diag) % 10000019
        total_num_with_diags = (total_num_with_diags + num_with_diag) % 10000019

        start_diag_pt, end_diag_pt = end_diag_pt, start_diag_pt
        num_to_start_diag = comp_num_path_in_rect((0,0), start_diag_pt)
        num_from_end_diag = comp_num_path_in_rect(end_diag_pt, (width, height))
        num_with_diag = (num_to_start_diag * num_from_end_diag) % 10000019
        total_num_with_diags = (total_num_with_diags + num_with_diag) % 10000019

    return total_num_with_diags

def comp_num_path_in_rect(start_pt, end_pt):
    w = end_pt[0] - start_pt[0]
    h = end_pt[1] - start_pt[1]
    return int(math.factorial(w+h) / (math.factorial(w) * math.factorial(h))) % 10000019

print(solution(2, 2, [[1, 1], [2, 2]]))