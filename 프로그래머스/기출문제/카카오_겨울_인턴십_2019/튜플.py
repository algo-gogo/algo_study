def solution(S):
    S = S[2:-2].split("},{")
    print(S)
    numArr = []
    for i in range(len(S)):
        s = S[i].split(",")
        numArr.append(set(s))

    numArr.sort(key=lambda x: len(x))

    print("adsf", numArr)
    ans = set()
    res = []
    for a in numArr:
        tmp = a - ans
        res.append(list(tmp)[0])
        ans = ans | tmp

    res = [int(i) for i in res]
    return res

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))