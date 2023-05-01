# 방학을 맞아 코딩이는 배달 아르바이트를 시작하기로 결심했다.
# 코딩이는 효율적인 배달 서비스를 제공하기 위해 배달 도우미 앱을 개발하려고 한다.
# 코딩이는 최단거리 조회 기능을 필수 기능으로 생각하고 현재 위치에서 목적지까지의 최단 거리를 알려주는 기능을 개발하려고 한다.
# 코딩이를 도와 최단거리 조회 기능을 완성하라.
#
# 2차원 맵(Mn*m)과 현재 위치 좌표(Sx, Sy)와 배달지 좌표(Dx, Dy)가 주어졌을 때, 현재 위치에서 목적지까지의 최단거리를 계산해야한다.
#
# 2차원 맵(Mn*m)은 지도를 단순화시킨 정보로 0 혹은 1 값으로만 이루어져있다.
# 지도 값의 0은 도로, 1은 건물을 의미하며 배달원은 도로로만 주행이 가능하며 건물을 통과할 수 없다.
# 지도는 항상 사각형 모양으로만 제공된다.


from collections import deque


def solution(M, S, D):
    # Get the dimensions of the map
    n, m = len(M), len(M[0])

    # Define the directions of movement: up, down, left, and right
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Create a queue for BFS
    queue = deque()
    queue.append((S[1], S[0], 0))  # (x, y, distance)

    visited = set()

    while queue:
        x, y, distance = queue.popleft()

        if (x, y) == (D[1], D[0]):
            return distance

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if M[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, distance + 1))

    # If the destination is not reachable, return -1
    return -1

print(solution([[0, 0, 0],[0, 1, 0],[0, 0, 0]], [0, 0], [2, 2]))
print(solution([[0, 0, 1, 0, 0, 0, 0, 0],[0, 0, 0, 1, 0, 1, 0, 0],[0, 0, 0, 1, 0, 1, 0, 0], [0, 1, 1, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
               , [0, 0], [6, 3]))

