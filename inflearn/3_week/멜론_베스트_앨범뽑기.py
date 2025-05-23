def solution(genres, plays):
    answer = []

    dict = {}
    num_dict = {}
    for i in range(len(genres)):
        dict[genres[i]] = []
        num_dict[genres[i]] = 0

    for i in range(len(genres)):
        dict[genres[i]].append((i, plays[i]))
        num_dict[genres[i]] += plays[i]

    for key in dict:
        if len(dict[key]) > 1:
            dict[key].sort(key=lambda x: (x[1],x[0]), reverse=True)

    if len(num_dict) > 1:
        num_dict = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)

    print('dict', dict)
    print('num_dict', num_dict)
    for key_tuple in num_dict:
        for i in range(len(dict[key_tuple[0]])):
            if i >= 2:
                break
            answer.append(dict[key_tuple[0]][i][0])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 500, 200]))