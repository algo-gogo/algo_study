def solution(words, queries):
    resultList = []

    for i in queries:
        result = 0
        for j in words:
            if len(i) == len(j):
                splitList = i.split('?')
                if splitList[0] == '' and splitList[-1] == '':
                    result += 1
                elif splitList[0] != '':
                    if j.startswith(splitList[0]):
                        result += 1
                else:
                    if j.endswith(splitList[-1]):
                        result += 1
        resultList.append(result)
    return resultList


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["fro??", "????o", "fr???", "fro???", "pro?"]))
