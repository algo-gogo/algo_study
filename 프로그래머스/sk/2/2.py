def solve_processes(processes, processes_num):
    split = processes[processes_num].split(' ')
    type = split[0]
    start_time = int(split[1])
    end_time = int(split[2])
    index1 = int(split[3])
    index2 = int(split[4])
    index3 = 0
    if type == 'write':
        index3 = int(split[5])
    return type, start_time, end_time, index1, index2, index3

# run_process 에 들어갈 수 있는지
def check_process(run_process, type):
    if len(run_process) == 0:
        return True
    for i in run_process:
        ## 쓰기 작업중이면 false
        if i[0] == 'write':
            return False
        ## 읽기 작업중인데 type이 read 면 가능
        elif type == 'read':
            return True
        ## 읽기 작업중인데 type이 write면 불가능
        else:
            return False

def out_ready_process(ready_process, s_process):
    if len(ready_process) == 0:
        return s_process
    else:
        flag = False
        for i in range(len(ready_process)):
            if ready_process[i][0] == 'read':
                pass
            elif ready_process[i][0] == 'write':
                flag = True
                return ready_process[i]

        if not flag:
            return ready_process[0]


def solution(arr, processes):

    time = 0
    processes_num = 0
    run_process = []
    ready_process = []
    while True:
        time += 1
        s_process = solve_processes(processes, processes_num)
        # 시간이 되면 작업, 대기 프로세스에 넣기
        if s_process[1] == time:
            if check_process(run_process, s_process[0]):
                process = out_ready_process(ready_process, s_process)
                run_process.append(process)
            else:
                ready_process.append(s_process)

        # 시간이 다되면 작업 프로세스에서 제거 하고 쓴다.

        print(run_process)
        print(ready_process)
        if time == 13:
            break


    answer = []
    return answer


# read 1 3 1 2
#     요청시각, 해당 요청 처리 시간, 배열의 인덱스

# write 4 3 3 5 2
#      요청시각, 해당 요청 처리 시간, 배열의 인덱스 , 배열의 인덱스 배열 구간에 쓸 한자리 숫자
print(solution(["1", "2", "4", "3", "3", "4", "1", "5"],
               ["read 1 3 1 2", "read 2 6 4 7", "write 4 3 3 5 2", "read 5 2 2 5", "write 6 1 3 3 9", "read 9 1 0 7"]))
