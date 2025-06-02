from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

# →, ←, ↑, ↓
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def count_check(count):
    if count <= 10:
        return True
    else:
        return False

def is_available_to_take_out_only_red_marble(game_map):
    queue = deque()

    count = 0
    for i in range(len(game_map)):
        for j in range(len(game_map[0])):
            if game_map[i][j] == 'R':
                queue.append((i, j))
    for i in range(len(game_map)):
        for j in range(len(game_map[0])):
            if game_map[i][j] == 'B':
                queue[0] = queue[0] + (i, j, count)

    print(queue)
    while queue:
        rx, ry, bx, by, count = queue.popleft()
        for i in range(4):
            rnx = rx + dx[i]
            rny = ry + dy[i]
            bnx = bx + dx[i]
            bny = by + dy[i]
            # 빨, 파 둘다 이동 가능
            if (0 <= rnx < len(game_map) and 0 <= rny < len(game_map[0]) and game_map[rnx][rny] != '#'
                    and 0 <= bnx < len(game_map) and 0 <= bny < len(game_map[0]) and game_map[bnx][bny] != '#'):
                if game_map[rnx][rny] == 'O':
                    return False
                queue.append((rnx, rny, bnx, bny, count + 1))
            # 빨은 이동 불가능, 파는 이동 가능
            elif (0 > rnx or rny >= len(game_map) or game_map[rnx][rny] == '#' or 0 > rny or rny >= len(game_map[0])) and 0 <= bnx < len(game_map) and 0 <= bny < len(game_map[0]) and game_map[bnx][bny] != '#':
                if game_map[bnx][bny] == 'O':
                    continue
                # 파가 이동 가능하지만 거기에 빨이 있을 경우
                if rx == bnx and ry == bny:
                    queue.append((rx, ry, bx, by, count + 1))
                else:
                    queue.append((rx, ry, bnx, bny, count + 1))
            # 빨은 이동 가능, 파는 이동 불가능
            elif (0 > bnx or bny >= len(game_map) or game_map[bnx][bny] == '#' or 0 > bny or bny >= len(
                game_map[0])) and 0 <= rnx < len(game_map) and 0 <= rny < len(game_map[0]) and game_map[rnx][
                rny] != '#':
                if game_map[rnx][rny] == 'O':
                    return count_check(count)
                if bx == rnx and by == rny:
                    queue.append((rx, ry, bx, by, count + 1))
                else:
                    queue.append((rx, ry, rnx, rny, count + 1))
            # 모두 못움직일 경우
            elif (0 > bnx or bny >= len(game_map) or game_map[bnx][bny] == '#' or 0 > bny or bny >= len(game_map[0])
                or 0 > rnx or rny >= len(game_map) or game_map[rnx][rny] == '#' or 0 > rny or rny >= len(game_map[0])):
                return False

    return count_check(count)


print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다



game_map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = False / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
["#", "#", "#", "#", "#", "#", "#"],
["#", ".", ".", "R", "#", "B", "#"],
["#", ".", "#", "#", "#", "#", "#"],
["#", ".", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", ".", "#"],
["#", "O", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))