def solution(files):
    answer = []

    result_list = []
    for file in files:

        head_index = 0
        head = ''
        number = ''
        for i in range(len(file)):
            if file[i].isdigit():
                head_index = i
                head = file[:i]
                head = head.lower()
                break
        for i in range(head_index, len(file)):
            if file[i].isdigit():
                number += file[i]
            else:
                break

        print(head, number)
        result_list.append([head, int(number), file])

    result_list.sort(key=lambda x: (x[0], int(x[1])))
    print(result_list)
    for result in result_list:
        answer.append(result[2])

    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
