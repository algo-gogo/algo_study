def dfs(x, y, places, visited):
    if 0 <= x < 5 and 0 <= y < 5:
        if not visited[x][y]:
            visited[x][y] = True
            if places[x][y] == 'P':
                return False
            if places[x][y] == 'X':
                return True
            elif places[x][y] == 'O':
                if not dfs(x-1, y, places, visited):
                    return False
                if not dfs(x+1, y, places, visited):
                    return False
                if not dfs(x, y-1, places, visited):
                    return False
                if not dfs(x, y+1, places, visited):
                    return False
                return True
            return True
        return True
    else:
        return True

def check(places):
    place_list = []

    for i in range(len(places)):
        for j in range(len(places[i])):
            if places[i][j] == 'P':
                place_list.append((i, j))
    print(place_list)

    visited = [[False] * 5 for _ in range(5)]

    result_list = []
    for p in place_list:
        x, y = p
        if not dfs(x-1, y, places, visited):
            result_list.append(False)
            continue
        if not dfs(x+1, y, places, visited):
            result_list.append(False)
            continue
        if not dfs(x, y-1, places, visited):
            result_list.append(False)
            continue
        if not dfs(x, y+1, places, visited):
            result_list.append(False)
            continue
        result_list.append(True)
    print(result_list)
    if False in result_list:
        return False
    return True

def solution(places):
    answer = []

    for i in range(len(places)):
        if not check(places[i]):
            answer.append(0)
        else:
            answer.append(1)

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
