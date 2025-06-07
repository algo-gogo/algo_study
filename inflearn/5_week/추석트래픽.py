### 다시 풀어야함
from datetime import datetime

def solution(lines):

    answer_list = []

    for i in range(len(lines)):
        answer = 1
        for j in range(i + 1, len(lines)):
            start_time = datetime.strptime(lines[i].split(' ')[0] + ' ' + lines[i].split(' ')[1], "%Y-%m-%d %H:%M:%S.%f")
            end_time = datetime.strptime(lines[j].split(' ')[0] + ' ' + lines[j].split(' ')[1], "%Y-%m-%d %H:%M:%S.%f")

            diff = end_time - start_time
            print(diff.total_seconds())
            time = float(lines[j].split(' ')[2][:-1])
            if diff.total_seconds() - time < 1:
                answer += 1
        answer_list.append(answer)
    return max(answer_list)

print(solution(["2016-09-15 01:00:04.001 2.0s","2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 01:00:04.002 2.0s","2016-09-15 01:00:07.000 2s"]))
print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))