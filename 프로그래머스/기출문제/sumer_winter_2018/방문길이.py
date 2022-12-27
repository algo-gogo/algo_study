def solution(dirs):

    x, y = 0, 0
    dx = {'U': 0, 'D': 0, 'R': 1, 'L': -1}
    dy = {'U': 1, 'D': -1, 'R': 0, 'L': 0}
    visited = set()
    for d in dirs:
        nx = x + dx[d]
        ny = y + dy[d]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            x = nx
            y = ny

    return len(visited) // 2

print(solution('ULURRDLLU'))
print(solution('LULLLLLLU'))