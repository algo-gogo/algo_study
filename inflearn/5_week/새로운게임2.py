k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def turn_back(direction):
    if direction == 0:
        return 1
    elif direction == 1:
        return 0
    elif direction == 2:
        return 3
    else:
        return 2

def find_horse_location(chess_horse_map, index):
    for i in range(len(chess_horse_map)):
        for j in range(len(chess_horse_map)):
            if index in chess_horse_map[i][j]:
                return i, j

def all_horse_location(chess_horse_map, horse_count):
    for i in range(len(chess_horse_map)):
        for j in range(len(chess_horse_map)):
            if len(chess_horse_map[i][j]) == horse_count:
                return True
    return False

def moving_horses(chess_horse_map, x, y, nx, ny, index):
    horse_stack = chess_horse_map[x][y]
    idx = horse_stack.index(index)
    moving_horses = horse_stack[idx:]
    chess_horse_map[nx][ny].extend(moving_horses)
    chess_horse_map[x][y] = horse_stack[:idx]
    return chess_horse_map

def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    chess_horse_map = [[[] for _ in range(len(game_map))] for _ in range(len(game_map))]
    for i, horse in enumerate(horse_location_and_directions):
        x, y, direction = horse
        chess_horse_map[x][y].append(i)

    # 0: 흰색 1: 빨강  2: 파랑
    print("game_map: ", game_map)
    print("chess_horse_map: ", chess_horse_map)

    # (행, 열, 인덱스)
    print("horse: ", horse_location_and_directions)

    turn_count = 0
    while all_horse_location(chess_horse_map, horse_count) is not True and turn_count < 1000:
        turn_count += 1
        print("turn_count: ", turn_count)
        for i in range(k):
            if all_horse_location(chess_horse_map, horse_count):
                break
            x, y = find_horse_location(chess_horse_map, i)
            direction = horse_location_and_directions[i][2]
            nx = x + dx[direction]
            ny = y + dy[direction]
            # 맵 안 + 0 또는 1
            if 0 <= nx < len(game_map) and 0 <= ny < len(game_map) and game_map[nx][ny] != 2:
                # 빨
                if game_map[nx][ny] == 1:
                    # chess_horse_map[nx][ny].extend(chess_horse_map[x][y])
                    # chess_horse_map[x][y] = []
                    chess_horse_map = moving_horses(chess_horse_map, x, y, nx, ny, i)
                    chess_horse_map.reverse()
                else:
                    # chess_horse_map[nx][ny].extend(chess_horse_map[x][y])
                    # chess_horse_map[x][y] = []
                    chess_horse_map = moving_horses(chess_horse_map, x, y, nx, ny, i)

            # 맵 밖 또는 파랑
            else:
                horse_location_and_directions[i][2] = turn_back(direction)
                direction = horse_location_and_directions[i][2]
                nx = x + dx[direction]
                ny = y + dy[direction]
                # 이동
                if 0 <= nx < len(game_map) and 0 <= ny < len(game_map):
                    # 파랑일 경우 가만히
                    if game_map[nx][ny] == 2:
                        pass
                    # 빨일 경우 옮긴 후 순서 뒤바꿈
                    elif game_map[nx][ny] == 1:
                        # chess_horse_map[nx][ny].extend(chess_horse_map[x][y])
                        # chess_horse_map[x][y] = []
                        chess_horse_map = moving_horses(chess_horse_map, x, y, nx, ny, i)
                        chess_horse_map[nx][ny].reverse()
                    # 0일 경우
                    else:
                        # chess_horse_map[nx][ny].extend(chess_horse_map[x][y])
                        # chess_horse_map[x][y] = []
                        chess_horse_map = moving_horses(chess_horse_map, x, y, nx, ny, i)
                # 방향 바꿔서 가려는데 맵 밖일 경우 가만히
                else:
                    pass

    return turn_count


print("정답 = 2 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다

start_horse_location_and_directions = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
print("정답 = 9 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

start_horse_location_and_directions = [
    [0, 1, 0],
    [0, 1, 1],
    [0, 1, 0],
    [2, 1, 2]
]
print("정답 = 3 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))