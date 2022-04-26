def solution(words, queries):
    result_list = []

    for i in queries:
        result = 0
        for j in words:
            if len(i) == len(j):
                split_list = i.split('?')
                if split_list[0] == '' and split_list[-1] == '':
                    result += 1
                elif split_list[0] != '':
                    if j.startswith(split_list[0]):
                        result += 1
                else:
                    if j.endswith(split_list[-1]):
                        result += 1
        result_list.append(result)
    return result_list색


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["fro??", "????o", "fr???", "fro???", "pro?"]))
