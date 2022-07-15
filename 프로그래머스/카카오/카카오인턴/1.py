def solution(survey, choices):
    choice_dic = {
        "R": 0, "T": 0, "C": 0, "F": 0,
        "J": 0, "M": 0, "A": 0, "N": 0
    }
    for index, value in enumerate(choices):
        choice_dic[survey[index][0]] += 4 - value

    result = ''

    result += "R" if choice_dic["R"] >= choice_dic["T"] else "T"
    result += "C" if choice_dic["C"] >= choice_dic["F"] else "F"
    result += "J" if choice_dic["J"] >= choice_dic["M"] else "M"
    result += "A" if choice_dic["A"] >= choice_dic["N"] else "N"

    return result


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], 	[7, 1, 3]))
