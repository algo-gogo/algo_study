def dfs(x, y, count, place, visited):
    if 0 <= x < 5 and 0 <= y < 5:
        if not visited[x][y]:
            visited[x][y] = True
            if place[x][y] == 'P':
                return False
            if place[x][y] == 'X':
                return True
            if count < 2:
                if not dfs(x - 1, y, count + 1, place, visited):
                    return False
                if not dfs(x + 1, y, count + 1, place, visited):
                    return False
                if not dfs(x, y - 1, count + 1, place, visited):
                    return False
                if not dfs(x, y + 1, count + 1, place, visited):
                    return False
                return True
            return True
        return True
    else:
        return True

# ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]
def find_place(place):
    place_list = []

    for i in range(len(place)):
        for j in range(len(place[i])):
            if place[i][j] == 'P':
                place_list.append((i, j, 0))

    print(place_list)
    result_list = []
    for x, y, count in place_list:
        visited = [[False for _ in range(5)] for _ in range(5)]
        print(visited)
        visited[x][y] = True
        if not dfs(x - 1, y, count + 1, place, visited):
            result_list.append(False)
            continue
        if not dfs(x + 1, y, count + 1, place, visited):
            result_list.append(False)
            continue
        if not dfs(x, y - 1, count + 1, place, visited):
            result_list.append(False)
            continue
        if not dfs(x, y + 1, count + 1, place, visited):
            result_list.append(False)
            continue
        result_list.append(True)

    if False in result_list:
        return False
    return True



def solution(places):
    answer = []
    for place in places:
        if not find_place(place):
            answer.append(0)
        else:
            answer.append(1)
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
