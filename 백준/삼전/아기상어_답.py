N = int(input())
shark = [0, 0]
# fishes = []
# fishes_dist = []
field = []

level = 2

neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def dist(start):
    open_node = [start]
    close_node = []
    dist_list = []
    distance = 0
    while len(open_node) and len(dist_list) == 0:
        distance += 1
        next_node = []
        for current in open_node:
            close_node.append(current)
            for neighbor in neighbors:
                i = current[0] + neighbor[0]
                j = current[1] + neighbor[1]
                if 0 <= i < N and 0 <= j < N and field[i][j] <= level and (i, j) not in close_node:
                    # close_node.append((i,j))
                    if field[i][j] != 0 and field[i][j] < level:
                        # return (distance, (i,j))
                        dist_list.append((distance, (i, j)))
                        close_node.append((i, j))
                    next_node.append((i, j))

        if len(dist_list) > 0:
            dist_list.sort(key=lambda x: (x[0], x[1][0]))
            return dist_list[0]
        open_node = next_node

    return None


for i in range(N):
    temp_row = list(map(int, input().split()))
    field.append(temp_row)

    for j in range(N):
        if temp_row[j] == 0:
            continue
        elif temp_row[j] == 9:
            shark = (i, j)
            temp_row[j] = 0

current_time = 0
exp = 0
fish = dist(shark)

while fish:
    # fish = fish_list[0]
    current_time += fish[0]
    exp += 1
    shark = fish[1]
    field[fish[1][0]][fish[1][1]] = 0
    if exp == level:
        exp = 0
        level += 1

    fish = dist(shark)

print(current_time)
