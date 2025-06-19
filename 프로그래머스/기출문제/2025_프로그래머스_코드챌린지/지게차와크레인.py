from copy import deepcopy

# 뚫려있는지 확인 => 뚫려있으면 True, 막혀있으면 False
def check(storage, i, j):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if nx < 0 or nx >= len(storage) or ny < 0 or ny >= len(storage[nx]) or storage[nx][ny] == '0':
            return True

    return False


def solution(storage, requests):
    answer = 0
    storage = [list(row) for row in storage]

    for request in requests:
        if len(request) > 1:
            for i in range(len(storage)):
                for j in range(len(storage[i])):
                    if storage[i][j] == request[0] and check(storage, i, j) is False:
                        storage[i][j] = '0+'
                    elif storage[i][j] == request[0]:
                        storage[i][j] = '0'
        else:
            temp_storage = deepcopy(storage)
            for i in range(len(storage)):
                for j in range(len(storage[i])):
                    if storage[i][j] == request[0] and check(temp_storage, i, j):
                        storage[i][j] = '0'

    print(storage)
    for i in range(len(storage)):
        for j in range(len(storage[i])):
            if storage[i][j] != '0' and storage[i][j] != '0+':
                answer += 1


    return answer

print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"]))
print(solution(["HAH", "HBH", "HHH", "HAH", "HBH"], ["C", "B", "B", "B", "B", "H"]))